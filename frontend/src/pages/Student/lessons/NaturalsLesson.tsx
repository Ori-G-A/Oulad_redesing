import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail, type LessonInteractionResult } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { Button } from "../../../components/ui/Button";
import { KatiaStorySlot } from "./KatiaStorySlot";
import { SetNodeScene } from "./SetNodeScene";
import "./NaturalsLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

const IDS = {
  total: "PREALG-N1-B04-Q01",
  enough: "PREALG-N1-B04-Q02",
  missing: "PREALG-N1-B04-Q03",
  classify: "PREALG-N1-B04-Q04",
} as const;

const CLASSIFY_OPTIONS = [
  "zero",
  "four",
  "negative_two",
  "sqrt_two",
  "fifteen",
  "decimal_25",
] as const;

const OPTION_MATH: Record<(typeof CLASSIFY_OPTIONS)[number], string> = {
  zero: "0",
  four: "4",
  negative_two: "-2",
  sqrt_two: String.raw`\sqrt{2}`,
  fifteen: "15",
  decimal_25: "2{,}5",
};

function restoredFeedback(id: string, selected: string, expected: boolean | null): string {
  if (id === IDS.total) return expected ? "total_correct" : "sum_again";
  if (id === IDS.enough) return selected === "no" ? "comparison_correct" : "eight_is_not_enough";
  if (id === IDS.missing) return expected ? "missing_correct" : "subtract_again";
  const values = new Set(selected.split(","));
  if (expected) return "naturals_correct";
  if (!values.has("zero")) return "zero_is_natural";
  if (values.has("negative_two")) return "negatives_are_not_natural";
  if (values.has("sqrt_two")) return "irrationals_not_natural";
  if (values.has("decimal_25")) return "decimals_not_natural";
  return "naturals_review";
}

export function NaturalsLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  const restored = lesson.progress.responses;
  const initialAnswers = Object.fromEntries(
    Object.entries(restored).map(([id, response]) => [id, response.selected_option]),
  );
  const initialAttempts = Object.fromEntries(
    Object.entries(restored).map(([id, response]) => [id, response.is_expected ? 2 : 1]),
  );
  const initialFeedback = Object.fromEntries(
    Object.entries(restored).map(([id, response]) => [
      id,
      restoredFeedback(id, response.selected_option, response.is_expected),
    ]),
  );

  const [answers, setAnswers] = useState<Record<string, string>>(initialAnswers);
  const [attempts, setAttempts] = useState<Record<string, number>>(initialAttempts);
  const [feedback, setFeedback] = useState<Record<string, string>>(initialFeedback);
  const [totalDraft, setTotalDraft] = useState(initialAnswers[IDS.total] ?? "");
  const [missingDraft, setMissingDraft] = useState(initialAnswers[IDS.missing] ?? "");
  const [selectedNaturals, setSelectedNaturals] = useState<Set<string>>(
    new Set((initialAnswers[IDS.classify] ?? "").split(",").filter(Boolean)),
  );
  const [zeroChallenge, setZeroChallenge] = useState("");

  const mutation = useMutation({
    mutationFn: ({ id, option }: { id: string; option: string }) =>
      studentApi.lessonInteraction(courseId, lesson.node_id, id, option),
    onSuccess: (result: LessonInteractionResult) => {
      setAnswers((current) => ({ ...current, [result.interaction_id]: result.selected_option }));
      setAttempts((current) => ({
        ...current,
        [result.interaction_id]: (current[result.interaction_id] ?? 0) + 1,
      }));
      setFeedback((current) => ({
        ...current,
        [result.interaction_id]: result.feedback_key,
      }));
    },
  });

  const isCorrect = (id: string) => {
    const response = restored[id];
    if (response && response.selected_option === answers[id]) return response.is_expected === true;
    if (id === IDS.total) return answers[id] === "8";
    if (id === IDS.enough) return answers[id] === "no";
    if (id === IDS.missing) return answers[id] === "2";
    return answers[id] === "fifteen,four,zero";
  };
  const resolved = (id: string) => isCorrect(id) || (attempts[id] ?? 0) >= 2;
  const allResolved = Object.values(IDS).every(resolved);

  const submit = (id: string, option: string) => mutation.mutate({ id, option });
  const toggleNatural = (option: string) => {
    if (resolved(IDS.classify)) return;
    setSelectedNaturals((current) => {
      const next = new Set(current);
      if (next.has(option)) next.delete(option);
      else next.add(option);
      return next;
    });
  };
  const classifyValue = CLASSIFY_OPTIONS.filter((option) => selectedNaturals.has(option))
    .sort()
    .join(",");

  const feedbackBlock = (id: string, answerKey: string) => {
    if (!feedback[id]) return null;
    const shouldReveal = !isCorrect(id) && (attempts[id] ?? 0) >= 2;
    return (
      <div className="trigger-feedback" role="status">
        <p>{t(`prealgebra.n1.b04.feedback.${feedback[id]}`)}</p>
        {!resolved(id) && <strong>{t("prealgebra.n1.b04.feedback.retry")}</strong>}
        {shouldReveal && <strong>{t(`prealgebra.n1.b04.feedback.reveal.${answerKey}`)}</strong>}
      </div>
    );
  };

  return (
    <article className="lesson-page naturals-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.safeZone")}</span>
      </header>

      <div className="lesson-shell naturals-shell">
        <header className="naturals-heading">
          <span className="lesson-kicker">{t("prealgebra.n1.b04.kicker")}</span>
          <h1 id="lesson-title">{t("prealgebra.n1.b04.title")}</h1>
          <p>{t(`prealgebra.n1.b04.intro.${lesson.presentation}`)}</p>
        </header>

        <SetNodeScene
          imageSrc="/prealgebra/step-naturales.png"
          activeStep="naturals"
          ariaLabel={t("prealgebra.n1.b04.setAria")}
        />

        <KatiaStorySlot
          eyebrow={t("prealgebra.n1.b04.story.katiaEyebrow")}
          title={t("prealgebra.n1.b04.story.katiaTitle")}
          body={t("prealgebra.n1.b04.story.katiaBody")}
          question={t("prealgebra.n1.b04.story.katiaQuestion")}
        />

        <section className="set-story" aria-label={t("prealgebra.n1.b04.story.label")}>
          <article>
            <span>{t("prealgebra.n1.b04.story.discoveryEyebrow")}</span>
            <h2>{t("prealgebra.n1.b04.story.discoveryTitle")}</h2>
            <p>{t("prealgebra.n1.b04.story.discoveryBody")}</p>
          </article>
          <article className="set-formal">
            <span>{t("prealgebra.n1.b04.story.definitionEyebrow")}</span>
            <h2>{t("prealgebra.n1.b04.story.definitionTitle")}</h2>
            <MathFormula math={String.raw`\mathbb{N}=\{0,1,2,3,\ldots\}`} />
            <p>{t("prealgebra.n1.b04.story.definitionBody")}</p>
          </article>
        </section>

        <section className="set-base-examples set-examples-standalone" aria-label={t("prealgebra.n1.b04.story.examplesLabel")}>
          {(["count", "zero", "trap"] as const).map((example) => (
            <article key={example}>
              <span>{t(`prealgebra.n1.b04.story.examples.${example}.eyebrow`)}</span>
              <h3>{t(`prealgebra.n1.b04.story.examples.${example}.title`)}</h3>
              <p>{t(`prealgebra.n1.b04.story.examples.${example}.body`)}</p>
              <ol>
                {[0, 1, 2].map((step) => (
                  <li key={step}>{t(`prealgebra.n1.b04.story.examples.${example}.steps.${step}`)}</li>
                ))}
              </ol>
            </article>
          ))}
        </section>

        <section className="bag-scenario" aria-labelledby="bag-title">
          <div className="bag-visual" aria-hidden="true">
            <span>3</span><i>+</i><span>5</span><i>→</i><b>10</b>
          </div>
          <div>
            <span>{t("prealgebra.n1.b04.scenario.eyebrow")}</span>
            <h2 id="bag-title">{t("prealgebra.n1.b04.scenario.title")}</h2>
            <p>{t("prealgebra.n1.b04.scenario.body")}</p>
          </div>
        </section>

        {lesson.presentation !== "avanzado" && (
          <section className="worked-path" aria-label={t("prealgebra.n1.b04.worked.label")}>
            <article className="revealed">
              <span>01</span><b>{t("prealgebra.n1.b04.worked.total")}</b>
              <MathFormula math="3+5=8" />
            </article>
            <article className={lesson.presentation === "basico" ? "revealed" : "faded"}>
              <span>02</span><b>{t("prealgebra.n1.b04.worked.enough")}</b>
              {lesson.presentation === "basico" ? <MathFormula math="8<10" /> : <em>?</em>}
            </article>
            <article className={lesson.presentation === "basico" ? "revealed" : "faded"}>
              <span>03</span><b>{t("prealgebra.n1.b04.worked.missing")}</b>
              {lesson.presentation === "basico" ? <MathFormula math="10-8=2" /> : <em>?</em>}
            </article>
          </section>
        )}

        <section className="naturals-practice" aria-label={t("prealgebra.n1.b04.practiceLabel")}>
          <article className="natural-question">
            <span className="question-number">01</span>
            <div>
              <h2>{t("prealgebra.n1.b04.q01.prompt")}</h2>
              <div className="numeric-answer">
                <input
                  type="number"
                  inputMode="numeric"
                  value={totalDraft}
                  disabled={resolved(IDS.total)}
                  aria-label={t("prealgebra.n1.b04.q01.inputAria")}
                  onChange={(event) => setTotalDraft(event.target.value)}
                />
                <Button
                  variant="secondary"
                  disabled={!totalDraft || resolved(IDS.total)}
                  loading={mutation.isPending}
                  onClick={() => submit(IDS.total, totalDraft)}
                >{t("prealgebra.n1.b04.check")}</Button>
              </div>
              {feedbackBlock(IDS.total, "total")}
            </div>
          </article>

          <article className="natural-question">
            <span className="question-number">02</span>
            <div>
              <h2>{t("prealgebra.n1.b04.q02.prompt")}</h2>
              <div className="choice-row">
                {(["yes", "no"] as const).map((option) => (
                  <button
                    key={option}
                    className={answers[IDS.enough] === option ? "selected" : ""}
                    disabled={resolved(IDS.enough) || mutation.isPending}
                    aria-pressed={answers[IDS.enough] === option}
                    onClick={() => submit(IDS.enough, option)}
                  >{t(`prealgebra.n1.b04.q02.options.${option}`)}</button>
                ))}
              </div>
              {feedbackBlock(IDS.enough, "enough")}
            </div>
          </article>

          <article className="natural-question">
            <span className="question-number">03</span>
            <div>
              <h2>{t("prealgebra.n1.b04.q03.prompt")}</h2>
              <div className="numeric-answer">
                <input
                  type="number"
                  inputMode="numeric"
                  value={missingDraft}
                  disabled={resolved(IDS.missing)}
                  aria-label={t("prealgebra.n1.b04.q03.inputAria")}
                  onChange={(event) => setMissingDraft(event.target.value)}
                />
                <Button
                  variant="secondary"
                  disabled={!missingDraft || resolved(IDS.missing)}
                  loading={mutation.isPending}
                  onClick={() => submit(IDS.missing, missingDraft)}
                >{t("prealgebra.n1.b04.check")}</Button>
              </div>
              {feedbackBlock(IDS.missing, "missing")}
            </div>
          </article>

          <article className="natural-question classify-question">
            <span className="question-number">04</span>
            <div>
              <h2>{t("prealgebra.n1.b04.q04.prompt")}</h2>
              <div className="number-choices" role="group" aria-label={t("prealgebra.n1.b04.q04.groupAria")}>
                {CLASSIFY_OPTIONS.map((option) => (
                  <button
                    key={option}
                    className={selectedNaturals.has(option) ? "selected" : ""}
                    disabled={resolved(IDS.classify)}
                    aria-pressed={selectedNaturals.has(option)}
                    aria-label={t(`prealgebra.n1.b04.q04.aria.${option}`)}
                    onClick={() => toggleNatural(option)}
                  >
                    <MathFormula math={OPTION_MATH[option]} />
                  </button>
                ))}
              </div>
              <Button
                variant="secondary"
                disabled={!classifyValue || resolved(IDS.classify)}
                loading={mutation.isPending}
                onClick={() => submit(IDS.classify, classifyValue)}
              >{t("prealgebra.n1.b04.checkSelection")}</Button>
              {feedbackBlock(IDS.classify, "classify")}
            </div>
          </article>
        </section>

        {allResolved && lesson.presentation === "avanzado" && (
          <section className="zero-challenge">
            <span>{t("prealgebra.n1.b04.challenge.eyebrow")}</span>
            <h2>{t("prealgebra.n1.b04.challenge.title")}</h2>
            <div className="choice-row">
              {(["absence", "first"] as const).map((option) => (
                <button
                  key={option}
                  className={zeroChallenge === option ? "selected" : ""}
                  disabled={Boolean(zeroChallenge)}
                  onClick={() => setZeroChallenge(option)}
                >{t(`prealgebra.n1.b04.challenge.options.${option}`)}</button>
              ))}
            </div>
            {zeroChallenge && (
              <p className="trigger-feedback" role="status">
                {t(`prealgebra.n1.b04.challenge.feedback.${zeroChallenge}`)}
              </p>
            )}
          </section>
        )}

        <footer className="lesson-footer trigger-footer">
          <div>
            <span>{t("prealgebra.n1.b04.footerLabel")}</span>
            <p>{t("prealgebra.n1.b04.footerBody")}</p>
          </div>
          <Button size="lg" disabled={!allResolved} loading={finishing} onClick={onFinish}>
            {lesson.state === "completed" ? t("prealgebra.backToMap") : t("prealgebra.n1.b04.finish")}
          </Button>
        </footer>
      </div>
    </article>
  );
}
