import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { Button } from "../../../components/ui/Button";
import { KatiaStorySlot } from "./KatiaStorySlot";
import { SetNodeScene } from "./SetNodeScene";
import "./RationalsLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

const IDS = {
  fraction: "PREALG-N1-B06-Q01",
  division: "PREALG-N1-B06-Q02",
  decimal: "PREALG-N1-B06-Q03",
  classify: "PREALG-N1-B06-Q04",
} as const;

const EXPECTED: Record<string, string> = {
  [IDS.fraction]: "three_fourths",
  [IDS.division]: "three_div_four",
  [IDS.decimal]: "decimal_075",
  [IDS.classify]: "dec_025,frac_34,neg3,periodic_0333",
};

const CLASSIFY_OPTIONS = ["frac_34", "dec_025", "neg3", "periodic_0333", "sqrt2", "pi"] as const;
const CLASSIFY_MATH: Record<(typeof CLASSIFY_OPTIONS)[number], string> = {
  frac_34: String.raw`\frac{3}{4}`,
  dec_025: "0{,}25",
  neg3: "-3",
  periodic_0333: String.raw`0{,}\overline{3}`,
  sqrt2: String.raw`\sqrt{2}`,
  pi: String.raw`\pi`,
};

const OPTION_MATH: Record<string, string> = {
  three_fourths: String.raw`\frac{3}{4}`,
  four_thirds: String.raw`\frac{4}{3}`,
  add: "3+4",
  subtract: "4-3",
  three_div_four: String.raw`3\div4`,
  four_div_three: String.raw`4\div3`,
  decimal_075: "0{,}75",
  repeating_0333: String.raw`0{,}\overline{3}`,
  decimal_34: "3{,}4",
  decimal_43: "4{,}3",
};

function feedbackFor(id: string, option: string): string {
  const keys: Record<string, string> = {
    three_fourths: "sharing_fraction_correct",
    four_thirds: "numerator_denominator_order",
    add: id === IDS.fraction ? "sharing_not_total" : "fraction_means_division",
    subtract: id === IDS.fraction ? "sharing_not_difference" : "fraction_means_division",
    three_div_four: "division_order_correct",
    four_div_three: "divide_numerator_by_denominator",
    decimal_075: "decimal_correct",
    repeating_0333: "one_third_repeats",
    decimal_34: "perform_division",
    decimal_43: "perform_division",
  };
  return keys[option];
}

function classifyFeedback(selected: string): string {
  const v = new Set(selected.split(","));
  if (selected === "dec_025,frac_34,neg3,periodic_0333") return "rationals_all_correct";
  if (!v.has("neg3")) return "omitted_integer";
  if (!v.has("periodic_0333")) return "omitted_periodic";
  if (v.has("sqrt2") || v.has("pi")) return "included_irrational";
  return "rationals_review";
}

export function RationalsLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  const restored = lesson.progress.responses;
  const [answers, setAnswers] = useState<Record<string, string>>(
    Object.fromEntries(Object.entries(restored).map(([id, response]) => [id, response.selected_option])),
  );
  const [attempts, setAttempts] = useState<Record<string, number>>(
    Object.fromEntries(Object.entries(restored).map(([id, response]) => [id, response.is_expected ? 2 : 1])),
  );
  const [feedback, setFeedback] = useState<Record<string, string>>(
    Object.fromEntries(Object.entries(restored).map(([id, response]) => [
      id,
      id === IDS.classify ? classifyFeedback(response.selected_option) : feedbackFor(id, response.selected_option),
    ])),
  );
  const [periodicChallenge, setPeriodicChallenge] = useState("");
  const [selectedRationals, setSelectedRationals] = useState<Set<string>>(
    new Set((restored[IDS.classify]?.selected_option ?? "").split(",").filter(Boolean)),
  );

  const mutation = useMutation({
    mutationFn: ({ id, option }: { id: string; option: string }) =>
      studentApi.lessonInteraction(courseId, lesson.node_id, id, option),
    onSuccess: (result) => {
      setAnswers((current) => ({ ...current, [result.interaction_id]: result.selected_option }));
      setAttempts((current) => ({ ...current, [result.interaction_id]: (current[result.interaction_id] ?? 0) + 1 }));
      setFeedback((current) => ({ ...current, [result.interaction_id]: result.feedback_key }));
    },
  });

  const correct = (id: string) => answers[id] === EXPECTED[id];
  const resolved = (id: string) =>
    id === IDS.decimal ? Boolean(answers[id]) : correct(id) || (attempts[id] ?? 0) >= 2;
  const allResolved = Object.values(IDS).every(resolved);

  const submit = (id: string, option: string) => mutation.mutate({ id, option });
  const toggleRational = (option: string) => {
    if (resolved(IDS.classify)) return;
    setSelectedRationals((cur) => {
      const next = new Set(cur);
      if (next.has(option)) next.delete(option);
      else next.add(option);
      return next;
    });
  };
  const classifyValue = CLASSIFY_OPTIONS.filter((o) => selectedRationals.has(o)).sort().join(",");
  const renderOptions = (id: string, options: string[]) => (
    <div className="rational-options">
      {options.map((option) => (
        <button
          key={option}
          className={answers[id] === option ? "selected" : ""}
          disabled={resolved(id) || mutation.isPending}
          aria-pressed={answers[id] === option}
          aria-label={t(`prealgebra.n1.b06.optionsAria.${option}`)}
          onClick={() => submit(id, option)}
        >
          <MathFormula math={OPTION_MATH[option]} />
        </button>
      ))}
    </div>
  );

  const feedbackBlock = (id: string, reveal: string) => {
    if (!feedback[id]) return null;
    const mayRetry = id !== IDS.decimal && !resolved(id);
    return (
      <div className="trigger-feedback" role="status">
        <p>{t(`prealgebra.n1.b06.feedback.${feedback[id]}`)}</p>
        {mayRetry && <strong>{t("prealgebra.n1.b06.feedback.retry")}</strong>}
        {!correct(id) && resolved(id) && (
          <strong>{t(`prealgebra.n1.b06.feedback.reveal.${reveal}`)}</strong>
        )}
      </div>
    );
  };

  return (
    <article className="lesson-page rationals-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.safeZone")}</span>
      </header>
      <div className="lesson-shell rationals-shell">
        <header className="rationals-heading">
          <span className="lesson-kicker">{t("prealgebra.n1.b06.kicker")}</span>
          <h1 id="lesson-title">{t("prealgebra.n1.b06.title")}</h1>
          <p>{t(`prealgebra.n1.b06.intro.${lesson.presentation}`)}</p>
        </header>

        <SetNodeScene
          imageSrc="/prealgebra/step-racionales.png"
          activeStep="rationals"
          ariaLabel={t("prealgebra.n1.b06.setAria")}
        />

        <KatiaStorySlot
          eyebrow={t("prealgebra.n1.b06.story.katiaEyebrow")}
          title={t("prealgebra.n1.b06.story.katiaTitle")}
          body={t("prealgebra.n1.b06.story.katiaBody")}
          formulas={[
            { math: String.raw`\frac{2}{3}`, caption: t("prealgebra.n1.b06.story.katiaFractionA") },
            { math: String.raw`\frac{1}{4}`, caption: t("prealgebra.n1.b06.story.katiaFractionB") },
          ]}
          question={t("prealgebra.n1.b06.story.katiaQuestion")}
        />

        <section className="set-story" aria-label={t("prealgebra.n1.b06.story.label")}>
          <article>
            <span>{t("prealgebra.n1.b06.story.discoveryEyebrow")}</span>
            <h2>{t("prealgebra.n1.b06.story.discoveryTitle")}</h2>
            <p>{t("prealgebra.n1.b06.story.discoveryBody")}</p>
          </article>
          <article className="set-formal">
            <span>{t("prealgebra.n1.b06.story.definitionEyebrow")}</span>
            <h2>{t("prealgebra.n1.b06.story.definitionTitle")}</h2>
            <MathFormula math={String.raw`\mathbb{Q}=\left\{\frac{a}{b}:a,b\in\mathbb{Z},\ b\ne0\right\}`} />
            <p>{t("prealgebra.n1.b06.story.definitionBody")}</p>
          </article>
        </section>

        <section className="set-base-examples set-examples-standalone" aria-label={t("prealgebra.n1.b06.story.examplesLabel")}>
          {(["share", "integer", "trap"] as const).map((example) => (
            <article key={example}>
              <span>{t(`prealgebra.n1.b06.story.examples.${example}.eyebrow`)}</span>
              <h3>{t(`prealgebra.n1.b06.story.examples.${example}.title`)}</h3>
              <p>{t(`prealgebra.n1.b06.story.examples.${example}.body`)}</p>
              <ol>
                {[0, 1, 2].map((step) => (
                  <li key={step}>{t(`prealgebra.n1.b06.story.examples.${example}.steps.${step}`)}</li>
                ))}
              </ol>
            </article>
          ))}
        </section>

        <section className="bread-scenario" aria-labelledby="bread-title">
          <div className="bread-visual" aria-hidden="true">
            {[0, 1, 2].map((bread) => <span key={bread}><i></i><i></i><i></i><i></i></span>)}
          </div>
          <div>
            <span>{t("prealgebra.n1.b06.scenario.eyebrow")}</span>
            <h2 id="bread-title">{t("prealgebra.n1.b06.scenario.title")}</h2>
            <p>{t("prealgebra.n1.b06.scenario.body")}</p>
          </div>
        </section>

        {lesson.presentation !== "avanzado" && (
          <section className="equivalence-path" aria-label={t("prealgebra.n1.b06.worked.label")}>
            <div><span>{t("prealgebra.n1.b06.worked.share")}</span><MathFormula math={String.raw`\frac{3}{4}`} /></div>
            <b aria-hidden="true">=</b>
            <div className={lesson.presentation === "basico" ? "" : "faded"}><span>{t("prealgebra.n1.b06.worked.division")}</span>{lesson.presentation === "basico" ? <MathFormula math={String.raw`3\div4`} /> : <em>?</em>}</div>
            <b aria-hidden="true">=</b>
            <div className={lesson.presentation === "basico" ? "" : "faded"}><span>{t("prealgebra.n1.b06.worked.decimal")}</span>{lesson.presentation === "basico" ? <MathFormula math="0{,}75" /> : <em>?</em>}</div>
          </section>
        )}

        <section className="naturals-practice" aria-label={t("prealgebra.n1.b06.practiceLabel")}>
          <article className="natural-question"><span className="question-number">01</span><div><h2>{t("prealgebra.n1.b06.q01.prompt")}</h2>{renderOptions(IDS.fraction, ["three_fourths", "four_thirds", "add", "subtract"])}{feedbackBlock(IDS.fraction, "fraction")}</div></article>
          <article className="natural-question"><span className="question-number">02</span><div><h2>{t("prealgebra.n1.b06.q02.prompt")}</h2>{renderOptions(IDS.division, ["three_div_four", "four_div_three", "add", "subtract"])}{feedbackBlock(IDS.division, "division")}</div></article>
          <article className="natural-question"><span className="question-number">03</span><div><h2>{t("prealgebra.n1.b06.q03.prompt")}</h2>{renderOptions(IDS.decimal, ["decimal_075", "repeating_0333", "decimal_34", "decimal_43"])}{feedbackBlock(IDS.decimal, "decimal")}</div></article>
          <article className="natural-question">
            <span className="question-number">04</span>
            <div>
              <h2>{t("prealgebra.n1.b06.q04.prompt")}</h2>
              <div className="rational-options" role="group" aria-label={t("prealgebra.n1.b06.q04.groupAria")}>
                {CLASSIFY_OPTIONS.map((option) => (
                  <button
                    key={option}
                    className={selectedRationals.has(option) ? "selected" : ""}
                    disabled={resolved(IDS.classify)}
                    aria-pressed={selectedRationals.has(option)}
                    aria-label={t(`prealgebra.n1.b06.q04.aria.${option}`)}
                    onClick={() => toggleRational(option)}
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
              >{t("prealgebra.n1.b06.checkSelection")}</Button>
              {feedbackBlock(IDS.classify, "classify")}
            </div>
          </article>
        </section>

        {allResolved && lesson.presentation === "avanzado" && (
          <section className="periodic-challenge">
            <span>{t("prealgebra.n1.b06.challenge.eyebrow")}</span>
            <h2>{t("prealgebra.n1.b06.challenge.title")}</h2>
            <div className="periodic-equation"><MathFormula math={String.raw`0{,}\overline{3}=\frac{1}{3}`} /></div>
            <div className="choice-row">
              {(["rational", "irrational"] as const).map((option) => <button key={option} className={periodicChallenge === option ? "selected" : ""} disabled={Boolean(periodicChallenge)} onClick={() => setPeriodicChallenge(option)}>{t(`prealgebra.n1.b06.challenge.options.${option}`)}</button>)}
            </div>
            {periodicChallenge && <p className="trigger-feedback" role="status">{t(`prealgebra.n1.b06.challenge.feedback.${periodicChallenge}`)}</p>}
          </section>
        )}

        <footer className="lesson-footer trigger-footer">
          <div><span>{t("prealgebra.n1.b06.footerLabel")}</span><p>{t("prealgebra.n1.b06.footerBody")}</p></div>
          <Button size="lg" disabled={!allResolved} loading={finishing} onClick={onFinish}>{lesson.state === "completed" ? t("prealgebra.backToMap") : t("prealgebra.n1.b06.finish")}</Button>
        </footer>
      </div>
    </article>
  );
}
