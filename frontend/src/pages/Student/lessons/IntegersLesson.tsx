import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { motion } from "framer-motion";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { Button } from "../../../components/ui/Button";
import { KatiaStorySlot } from "./KatiaStorySlot";
import { SetNodeScene } from "./SetNodeScene";
import "./IntegersLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

const IDS = {
  debt: "PREALG-N1-B05-Q01",
  balance: "PREALG-N1-B05-Q02",
  representation: "PREALG-N1-B05-Q03",
  line: "PREALG-N1-B05-Q04",
  classify: "PREALG-N1-B05-Q05",
} as const;

const EXPECTED: Record<string, string> = {
  [IDS.debt]: "35000",
  [IDS.balance]: "5000",
  [IDS.representation]: "negative",
  [IDS.line]: "negative_5000",
  [IDS.classify]: "neg8,six,zero",
};

const CLASSIFY_OPTIONS = ["neg8", "neg_3_5", "zero", "half", "six", "neg_2_1"] as const;
const CLASSIFY_MATH: Record<(typeof CLASSIFY_OPTIONS)[number], string> = {
  neg8: "-8",
  neg_3_5: "-3{,}5",
  zero: "0",
  half: String.raw`\frac{1}{2}`,
  six: "6",
  neg_2_1: "-2{,}1",
};

const LINE_OPTIONS = ["negative_35000", "negative_5000", "zero", "positive_5000"] as const;
const LINE_POSITIONS: Record<string, number> = {
  negative_35000: 5,
  negative_5000: 57,
  zero: 76,
  positive_5000: 94,
};

function feedbackFor(id: string, selected: string): string {
  if (id === IDS.debt) return selected === "35000" ? "debt_total_correct" : "add_debts_again";
  if (id === IDS.balance) return selected === "5000" ? "balance_correct" : "payment_moves_to_zero";
  if (id === IDS.representation) {
    return selected === "negative"
      ? "negative_representation_correct"
      : selected === "zero"
        ? "zero_is_equilibrium"
        : "debt_is_below_zero";
  }
  if (id === IDS.classify) {
    const v = new Set(selected.split(","));
    if (selected === "neg8,six,zero") return "integers_correct";
    if (!v.has("zero")) return "zero_is_integer";
    if (v.has("neg_3_5") || v.has("neg_2_1")) return "decimal_not_integer";
    if (v.has("half")) return "fraction_not_integer";
    return "integers_review";
  }
  return selected === "negative_5000"
    ? "number_line_correct"
    : selected === "negative_35000"
      ? "payment_changes_position"
      : selected === "zero"
        ? "five_thousand_still_owed"
        : "debt_stays_negative";
}

export function IntegersLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  const restored = lesson.progress.responses;
  const initialAnswers = Object.fromEntries(
    Object.entries(restored).map(([id, response]) => [id, response.selected_option]),
  );
  const [answers, setAnswers] = useState<Record<string, string>>(initialAnswers);
  const [attempts, setAttempts] = useState<Record<string, number>>(
    Object.fromEntries(Object.entries(restored).map(([id, response]) => [id, response.is_expected ? 2 : 1])),
  );
  const [feedback, setFeedback] = useState<Record<string, string>>(
    Object.fromEntries(Object.entries(restored).map(([id, response]) => [id, feedbackFor(id, response.selected_option)])),
  );
  const [debtDraft, setDebtDraft] = useState(initialAnswers[IDS.debt] ?? "");
  const [balanceDraft, setBalanceDraft] = useState(initialAnswers[IDS.balance] ?? "");
  const [orderChallenge, setOrderChallenge] = useState("");
  const [selectedIntegers, setSelectedIntegers] = useState<Set<string>>(
    new Set((initialAnswers[IDS.classify] ?? "").split(",").filter(Boolean)),
  );

  const mutation = useMutation({
    mutationFn: ({ id, option }: { id: string; option: string }) =>
      studentApi.lessonInteraction(courseId, lesson.node_id, id, option),
    onSuccess: (result) => {
      setAnswers((current) => ({ ...current, [result.interaction_id]: result.selected_option }));
      setAttempts((current) => ({
        ...current,
        [result.interaction_id]: (current[result.interaction_id] ?? 0) + 1,
      }));
      setFeedback((current) => ({ ...current, [result.interaction_id]: result.feedback_key }));
    },
  });

  const correct = (id: string) => answers[id] === EXPECTED[id];
  const resolved = (id: string) => correct(id) || (attempts[id] ?? 0) >= 2;
  const allResolved = Object.values(IDS).every(resolved);
  const submit = (id: string, option: string) => mutation.mutate({ id, option });
  const toggleInteger = (option: string) => {
    if (resolved(IDS.classify)) return;
    setSelectedIntegers((cur) => {
      const next = new Set(cur);
      if (next.has(option)) next.delete(option);
      else next.add(option);
      return next;
    });
  };
  const classifyValue = CLASSIFY_OPTIONS.filter((o) => selectedIntegers.has(o)).sort().join(",");

  const feedbackBlock = (id: string, answerKey: string) => {
    if (!feedback[id]) return null;
    return (
      <div className="trigger-feedback" role="status">
        <p>{t(`prealgebra.n1.b05.feedback.${feedback[id]}`)}</p>
        {!resolved(id) && <strong>{t("prealgebra.n1.b05.feedback.retry")}</strong>}
        {!correct(id) && (attempts[id] ?? 0) >= 2 && (
          <strong>{t(`prealgebra.n1.b05.feedback.reveal.${answerKey}`)}</strong>
        )}
      </div>
    );
  };

  const selectedLine = answers[IDS.line] ?? "negative_35000";

  return (
    <article className="lesson-page integers-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.safeZone")}</span>
      </header>

      <div className="lesson-shell integers-shell">
        <header className="integers-heading">
          <span className="lesson-kicker">{t("prealgebra.n1.b05.kicker")}</span>
          <h1 id="lesson-title">{t("prealgebra.n1.b05.title")}</h1>
          <p>{t(`prealgebra.n1.b05.intro.${lesson.presentation}`)}</p>
        </header>

        <SetNodeScene
          imageSrc="/prealgebra/step-enteros.png"
          activeStep="integers"
          ariaLabel={t("prealgebra.n1.b05.setAria")}
        />

        <KatiaStorySlot
          eyebrow={t("prealgebra.n1.b05.story.katiaEyebrow")}
          title={t("prealgebra.n1.b05.story.katiaTitle")}
          body={t("prealgebra.n1.b05.story.katiaBody")}
          question={t("prealgebra.n1.b05.story.katiaQuestion")}
        />

        <section className="set-story" aria-label={t("prealgebra.n1.b05.story.label")}>
          <article>
            <span>{t("prealgebra.n1.b05.story.discoveryEyebrow")}</span>
            <h2>{t("prealgebra.n1.b05.story.discoveryTitle")}</h2>
            <p>{t("prealgebra.n1.b05.story.discoveryBody")}</p>
          </article>
          <article className="set-formal">
            <span>{t("prealgebra.n1.b05.story.definitionEyebrow")}</span>
            <h2>{t("prealgebra.n1.b05.story.definitionTitle")}</h2>
            <MathFormula math={String.raw`\mathbb{Z}=\{\ldots,-3,-2,-1,0,1,2,3,\ldots\}`} />
            <p>{t("prealgebra.n1.b05.story.definitionBody")}</p>
          </article>
        </section>

        <section className="set-base-examples set-examples-standalone" aria-label={t("prealgebra.n1.b05.story.examplesLabel")}>
          {(["debt", "payment", "trap"] as const).map((example) => (
            <article key={example}>
              <span>{t(`prealgebra.n1.b05.story.examples.${example}.eyebrow`)}</span>
              <h3>{t(`prealgebra.n1.b05.story.examples.${example}.title`)}</h3>
              <p>{t(`prealgebra.n1.b05.story.examples.${example}.body`)}</p>
              <ol>
                {[0, 1, 2, 3].map((step) => (
                  <li key={step}>{t(`prealgebra.n1.b05.story.examples.${example}.steps.${step}`)}</li>
                ))}
              </ol>
            </article>
          ))}
        </section>

        <section className="debt-scenario" aria-labelledby="debt-title">
          <div className="receipt" aria-hidden="true">
            <span>{t("prealgebra.n1.b05.scenario.receipt")}</span>
            <b>$20.000</b><b>$15.000</b><i></i><strong>?</strong>
          </div>
          <div>
            <span>{t("prealgebra.n1.b05.scenario.eyebrow")}</span>
            <h2 id="debt-title">{t("prealgebra.n1.b05.scenario.title")}</h2>
            <p>{t("prealgebra.n1.b05.scenario.body")}</p>
          </div>
        </section>

        {lesson.presentation !== "avanzado" && (
          <section className="worked-path" aria-label={t("prealgebra.n1.b05.worked.label")}>
            <article className="revealed">
              <span>01</span><b>{t("prealgebra.n1.b05.worked.total")}</b>
              <MathFormula math="20{.}000+15{.}000=35{.}000" />
            </article>
            <article className={lesson.presentation === "basico" ? "revealed" : "faded"}>
              <span>02</span><b>{t("prealgebra.n1.b05.worked.payment")}</b>
              {lesson.presentation === "basico" ? <MathFormula math="35{.}000-30{.}000=5{.}000" /> : <em>?</em>}
            </article>
            <article className={lesson.presentation === "basico" ? "revealed" : "faded"}>
              <span>03</span><b>{t("prealgebra.n1.b05.worked.sign")}</b>
              {lesson.presentation === "basico" ? <MathFormula math="-5{.}000" /> : <em>?</em>}
            </article>
          </section>
        )}

        <section className="naturals-practice" aria-label={t("prealgebra.n1.b05.practiceLabel")}>
          <article className="natural-question">
            <span className="question-number">01</span>
            <div>
              <h2>{t("prealgebra.n1.b05.q01.prompt")}</h2>
              <div className="numeric-answer money-input">
                <span aria-hidden="true">$</span>
                <input type="number" inputMode="numeric" value={debtDraft} disabled={resolved(IDS.debt)} aria-label={t("prealgebra.n1.b05.q01.inputAria")} onChange={(event) => setDebtDraft(event.target.value)} />
                <Button variant="secondary" disabled={!debtDraft || resolved(IDS.debt)} loading={mutation.isPending} onClick={() => submit(IDS.debt, debtDraft)}>{t("prealgebra.n1.b05.check")}</Button>
              </div>
              {feedbackBlock(IDS.debt, "debt")}
            </div>
          </article>

          <article className="natural-question">
            <span className="question-number">02</span>
            <div>
              <h2>{t("prealgebra.n1.b05.q02.prompt")}</h2>
              <div className="numeric-answer money-input">
                <span aria-hidden="true">$</span>
                <input type="number" inputMode="numeric" value={balanceDraft} disabled={resolved(IDS.balance)} aria-label={t("prealgebra.n1.b05.q02.inputAria")} onChange={(event) => setBalanceDraft(event.target.value)} />
                <Button variant="secondary" disabled={!balanceDraft || resolved(IDS.balance)} loading={mutation.isPending} onClick={() => submit(IDS.balance, balanceDraft)}>{t("prealgebra.n1.b05.check")}</Button>
              </div>
              {feedbackBlock(IDS.balance, "balance")}
            </div>
          </article>

          <article className="natural-question">
            <span className="question-number">03</span>
            <div>
              <h2>{t("prealgebra.n1.b05.q03.prompt")}</h2>
              <div className="integer-options">
                {(["positive", "negative", "zero"] as const).map((option) => (
                  <button key={option} className={answers[IDS.representation] === option ? "selected" : ""} disabled={resolved(IDS.representation) || mutation.isPending} aria-pressed={answers[IDS.representation] === option} aria-label={t(`prealgebra.n1.b05.q03.aria.${option}`)} onClick={() => submit(IDS.representation, option)}>
                    <MathFormula math={option === "positive" ? "5{.}000" : option === "negative" ? "-5{.}000" : "0"} />
                  </button>
                ))}
              </div>
              {feedbackBlock(IDS.representation, "representation")}
            </div>
          </article>

          <KatiaStorySlot
            eyebrow="Recta numérica"
            title="Los enteros como etiquetas de referencia"
            body="Antes de ubicar la deuda restante, KatIA marca los enteros sobre la recta: el 0 es equilibrio, los negativos quedan a la izquierda y los positivos a la derecha. Esas etiquetas serán la referencia para leer después toda la recta real."
            imageSrc="/prealgebra/caso-enteros-recta.jpg"
            imageAlt="KatIA señala una recta numérica con enteros como referencia"
            formula={String.raw`\ldots,-2,-1,0,1,2,\ldots`}
          />

          <article className="natural-question line-question">
            <span className="question-number">04</span>
            <div>
              <h2>{t("prealgebra.n1.b05.q04.prompt")}</h2>
              <p className="line-instruction">{t("prealgebra.n1.b05.q04.instruction")}</p>
              <div className="integer-line" aria-label={t("prealgebra.n1.b05.q04.lineAria")}>
                <div className="line-track"></div>
                <motion.div className="line-marker" animate={{ left: `${LINE_POSITIONS[selectedLine]}%` }} transition={{ type: "spring", stiffness: 260, damping: 24 }} aria-hidden="true" />
                <div className="line-anchors">
                  {LINE_OPTIONS.map((option) => (
                    <button key={option} className={answers[IDS.line] === option ? "selected" : ""} disabled={resolved(IDS.line) || mutation.isPending} onClick={() => submit(IDS.line, option)} aria-label={t(`prealgebra.n1.b05.q04.aria.${option}`)}>
                      <span></span>{t(`prealgebra.n1.b05.q04.labels.${option}`)}
                    </button>
                  ))}
                </div>
              </div>
              {feedbackBlock(IDS.line, "line")}
            </div>
          </article>

          <article className="natural-question classify-question">
            <span className="question-number">05</span>
            <div>
              <h2>{t("prealgebra.n1.b05.q05.prompt")}</h2>
              <div className="number-choices" role="group" aria-label={t("prealgebra.n1.b05.q05.groupAria")}>
                {CLASSIFY_OPTIONS.map((option) => (
                  <button
                    key={option}
                    className={selectedIntegers.has(option) ? "selected" : ""}
                    disabled={resolved(IDS.classify)}
                    aria-pressed={selectedIntegers.has(option)}
                    aria-label={t(`prealgebra.n1.b05.q05.aria.${option}`)}
                    onClick={() => toggleInteger(option)}
                  >
                    <MathFormula math={CLASSIFY_MATH[option]} />
                  </button>
                ))}
              </div>
              <Button
                variant="secondary"
                disabled={!classifyValue || resolved(IDS.classify)}
                loading={mutation.isPending}
                onClick={() => submit(IDS.classify, classifyValue)}
              >{t("prealgebra.n1.b05.checkSelection")}</Button>
              {feedbackBlock(IDS.classify, "classify")}
            </div>
          </article>
        </section>

        {allResolved && lesson.presentation === "avanzado" && (
          <section className="zero-challenge">
            <span>{t("prealgebra.n1.b05.challenge.eyebrow")}</span>
            <h2>{t("prealgebra.n1.b05.challenge.title")}</h2>
            <div className="choice-row">
              {(["magnitude", "position"] as const).map((option) => (
                <button key={option} className={orderChallenge === option ? "selected" : ""} disabled={Boolean(orderChallenge)} onClick={() => setOrderChallenge(option)}>{t(`prealgebra.n1.b05.challenge.options.${option}`)}</button>
              ))}
            </div>
            {orderChallenge && <p className="trigger-feedback" role="status">{t(`prealgebra.n1.b05.challenge.feedback.${orderChallenge}`)}</p>}
          </section>
        )}

        <footer className="lesson-footer trigger-footer">
          <div><span>{t("prealgebra.n1.b05.footerLabel")}</span><p>{t("prealgebra.n1.b05.footerBody")}</p></div>
          <Button size="lg" disabled={!allResolved} loading={finishing} onClick={onFinish}>{lesson.state === "completed" ? t("prealgebra.backToMap") : t("prealgebra.n1.b05.finish")}</Button>
        </footer>
      </div>
    </article>
  );
}
