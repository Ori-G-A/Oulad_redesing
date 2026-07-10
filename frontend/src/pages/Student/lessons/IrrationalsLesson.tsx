/**
 * lessons/IrrationalsLesson.tsx — Nodo B07 (Irracionales · ℝ∖ℚ)
 * =============================================================
 * Define el irracional por "no es fracción" (no por el decimal): el patrón
 * decimal es pista, no criterio. Q01 reconoce el periódico (racional), Q02
 * distingue aproximación de valor exacto (π); el camino √2 en la recta (Q03)
 * se ofrece solo en banda avanzado. Reutiliza las clases de Lesson.css.
 */
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { Button } from "../../../components/ui/Button";
import { KatiaStorySlot } from "./KatiaStorySlot";
import { SetNodeScene } from "./SetNodeScene";
import "./IrrationalsLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

const IDS = {
  periodic: "PREALG-N1-B07-Q01",
  approx: "PREALG-N1-B07-Q02",
  sqrt2: "PREALG-N1-B07-Q03",
} as const;

const GRID = [
  { value: "dec05", math: "0{,}5", expected: "rational" },
  { value: "periodic03", math: String.raw`0{,}\overline{3}`, expected: "rational" },
  { value: "pi", math: String.raw`\pi`, expected: "irrational" },
  { value: "sqrt2", math: String.raw`\sqrt{2}`, expected: "irrational" },
  { value: "seven", math: "7", expected: "rational" },
] as const;
const gridId = (value: string) => `PREALG-N1-B07-G-${value}`;

const EXPECTED: Record<string, string> = {
  [IDS.periodic]: "periodic_0333",
  [IDS.approx]: "pi_approx",
  [IDS.sqrt2]: "between_1_2",
  ...Object.fromEntries(GRID.map((g) => [gridId(g.value), g.expected])),
};

function gridFeedback(value: string, selected: string): string {
  const item = GRID.find((g) => g.value === value);
  if (!item) return "";
  if (selected === item.expected) return "grid_correct";
  if (value === "periodic03") return "periodic_as_irrational";
  if (value === "seven") return "integer_as_irrational";
  if (value === "pi" || value === "sqrt2") return "irrational_as_rational";
  return "grid_review";
}

/** Opciones de Q01: decimales en LaTeX (las de Q02/Q03 son texto i18n). */
const OPTION_MATH: Record<string, string> = {
  exact_025: "0{,}25",
  periodic_0333: String.raw`0{,}\overline{3}`,
  nonperiodic_pi: String.raw`3{,}14159265\ldots`,
};

function feedbackFor(option: string): string {
  const keys: Record<string, string> = {
    periodic_0333: "periodic_correct",
    exact_025: "exact_not_periodic",
    nonperiodic_pi: "pi_not_periodic",
    pi_approx: "approx_correct",
    pi_exact: "approx_vs_exact",
    pi_ends: "pi_does_not_end",
    between_1_2: "sqrt2_between_correct",
    at_2: "sqrt2_not_2",
    between_2_3: "sqrt2_too_high",
  };
  return keys[option];
}

export function IrrationalsLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  const restored = lesson.progress.responses;
  const [answers, setAnswers] = useState<Record<string, string>>(
    Object.fromEntries(Object.entries(restored).map(([id, r]) => [id, r.selected_option])),
  );
  const [attempts, setAttempts] = useState<Record<string, number>>(
    Object.fromEntries(Object.entries(restored).map(([id, r]) => [id, r.is_expected ? 2 : 1])),
  );
  const [feedback, setFeedback] = useState<Record<string, string>>(
    Object.fromEntries(Object.entries(restored).map(([id, r]) => [
      id,
      id.includes("-G-") ? gridFeedback(id.replace("PREALG-N1-B07-G-", ""), r.selected_option) : feedbackFor(r.selected_option),
    ])),
  );

  const mutation = useMutation({
    mutationFn: ({ id, option }: { id: string; option: string }) =>
      studentApi.lessonInteraction(courseId, lesson.node_id, id, option),
    onSuccess: (result) => {
      setAnswers((c) => ({ ...c, [result.interaction_id]: result.selected_option }));
      setAttempts((c) => ({ ...c, [result.interaction_id]: (c[result.interaction_id] ?? 0) + 1 }));
      setFeedback((c) => ({ ...c, [result.interaction_id]: result.feedback_key }));
    },
  });

  const correct = (id: string) => answers[id] === EXPECTED[id];
  const resolved = (id: string) => correct(id) || (attempts[id] ?? 0) >= 2;
  const coreResolved = resolved(IDS.periodic) && resolved(IDS.approx);
  const gridAllResolved = GRID.every((g) => resolved(gridId(g.value)));
  const isAdvanced = lesson.presentation === "avanzado";

  const submit = (id: string, option: string) => mutation.mutate({ id, option });

  const feedbackBlock = (id: string, revealKey: string) => {
    if (!feedback[id]) return null;
    const mayRetry = !resolved(id);
    return (
      <div className="trigger-feedback" role="status">
        <p>{t(`prealgebra.n1.b07.feedback.${feedback[id]}`)}</p>
        {mayRetry && <strong>{t("prealgebra.n1.b07.feedback.retry")}</strong>}
        {!correct(id) && resolved(id) && (
          <strong>{t(`prealgebra.n1.b07.feedback.reveal.${revealKey}`)}</strong>
        )}
      </div>
    );
  };

  const mathOptions = (id: string, options: string[]) => (
    <div className="choice-stack">
      {options.map((option) => (
        <button
          key={option}
          className={answers[id] === option ? "selected" : ""}
          disabled={resolved(id) || mutation.isPending}
          aria-pressed={answers[id] === option}
          aria-label={t(`prealgebra.n1.b07.optionsAria.${option}`)}
          onClick={() => submit(id, option)}
        >
          <MathFormula math={OPTION_MATH[option]} />
        </button>
      ))}
    </div>
  );

  const textOptions = (id: string, group: "q02" | "q03", options: string[]) => (
    <div className="choice-stack">
      {options.map((option) => (
        <button
          key={option}
          className={answers[id] === option ? "selected" : ""}
          disabled={resolved(id) || mutation.isPending}
          aria-pressed={answers[id] === option}
          onClick={() => submit(id, option)}
        >
          {t(`prealgebra.n1.b07.${group}.options.${option}`)}
        </button>
      ))}
    </div>
  );

  return (
    <article className="lesson-page irrationals-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.safeZone")}</span>
      </header>

      <div className="lesson-shell">
        <header className="trigger-heading">
          <span className="lesson-kicker">{t("prealgebra.n1.b07.kicker")}</span>
          <h1 id="lesson-title">{t("prealgebra.n1.b07.title")}</h1>
          <p>{t(`prealgebra.n1.b07.intro.${lesson.presentation}`)}</p>
        </header>

        {/* Comparar tres decimales: dos vienen de fracción, uno no. */}
        <SetNodeScene
          imageSrc="/prealgebra/step-irracionales.png"
          activeStep="irrationals"
          ariaLabel={t("prealgebra.n1.b07.setAria")}
        />

        <KatiaStorySlot
          eyebrow={t("prealgebra.n1.b07.story.katiaEyebrow")}
          title={t("prealgebra.n1.b07.story.katiaTitle")}
          body={t("prealgebra.n1.b07.story.katiaBody")}
          question={t("prealgebra.n1.b07.story.katiaQuestion")}
          imageSrc="/prealgebra/generated/n1-agora/b07-irracionales-v4.png"
        />

        <section className="set-story" aria-label={t("prealgebra.n1.b07.story.label")}>
          <article>
            <span>{t("prealgebra.n1.b07.story.discoveryEyebrow")}</span>
            <h2>{t("prealgebra.n1.b07.story.discoveryTitle")}</h2>
            <p>{t("prealgebra.n1.b07.story.discoveryBody")}</p>
          </article>
          <article className="set-formal">
            <span>{t("prealgebra.n1.b07.story.definitionEyebrow")}</span>
            <h2>{t("prealgebra.n1.b07.story.definitionTitle")}</h2>
            <MathFormula math={String.raw`\mathbb{I}=\mathbb{R}\setminus\mathbb{Q}`} />
            <p>{t("prealgebra.n1.b07.story.definitionBody")}</p>
          </article>
        </section>

        <section className="set-base-examples set-examples-standalone" aria-label={t("prealgebra.n1.b07.story.examplesLabel")}>
          {(["exact", "periodic", "trap"] as const).map((example) => (
            <article key={example}>
              <span>{t(`prealgebra.n1.b07.story.examples.${example}.eyebrow`)}</span>
              <h3>{t(`prealgebra.n1.b07.story.examples.${example}.title`)}</h3>
              <p>{t(`prealgebra.n1.b07.story.examples.${example}.body`)}</p>
              <ol>
                {[0, 1, 2].map((step) => (
                  <li key={step}>{t(`prealgebra.n1.b07.story.examples.${example}.steps.${step}`)}</li>
                ))}
              </ol>
            </article>
          ))}
        </section>

        {!isAdvanced && (
          <section className="trigger-feedback" role="note">
            <p>{t("prealgebra.n1.b07.criterion")}</p>
          </section>
        )}

        <section aria-label={t("prealgebra.n1.b07.practiceLabel")}>
          <article className="trigger-question">
            <span className="question-number">01</span>
            <div>
              <h2>{t("prealgebra.n1.b07.q01.prompt")}</h2>
              {mathOptions(IDS.periodic, ["exact_025", "periodic_0333", "nonperiodic_pi"])}
              {feedbackBlock(IDS.periodic, "q01")}
            </div>
          </article>

          <article className="trigger-question">
            <span className="question-number">02</span>
            <div>
              <h2>{t("prealgebra.n1.b07.q02.prompt")}</h2>
              {textOptions(IDS.approx, "q02", ["pi_exact", "pi_approx", "pi_ends"])}
              {feedbackBlock(IDS.approx, "q02")}
            </div>
          </article>
        </section>

        <section className="irr-grid" aria-label={t("prealgebra.n1.b07.grid.label")}>
          <h2>{t("prealgebra.n1.b07.grid.prompt")}</h2>
          <ul className="irr-grid-list">
            {GRID.map((g) => {
              const id = gridId(g.value);
              const done = resolved(id);
              return (
                <li key={g.value} className="irr-grid-row">
                  <span className="irr-grid-num" aria-label={t(`prealgebra.n1.b07.grid.aria.${g.value}`)}>
                    <MathFormula math={g.math} />
                  </span>
                  <div className="irr-grid-choice" role="group" aria-label={t(`prealgebra.n1.b07.grid.aria.${g.value}`)}>
                    {(["rational", "irrational"] as const).map((option) => (
                      <button
                        key={option}
                        className={answers[id] === option ? "selected" : ""}
                        disabled={done || mutation.isPending}
                        aria-pressed={answers[id] === option}
                        onClick={() => submit(id, option)}
                      >
                        {t(`prealgebra.n1.b07.grid.${option}`)}
                      </button>
                    ))}
                  </div>
                  {feedback[id] && (
                    <p className={`irr-grid-feedback ${correct(id) ? "ok" : done ? "review" : ""}`} role="status">
                      {t(`prealgebra.n1.b07.grid.feedback.${feedback[id]}`)}
                    </p>
                  )}
                </li>
              );
            })}
          </ul>
        </section>

        {coreResolved && isAdvanced && (
          <section className="trigger-challenge">
            <span>{t("prealgebra.n1.b07.challenge.eyebrow")}</span>
            <h2>{t("prealgebra.n1.b07.challenge.title")}</h2>
            <p>{t("prealgebra.n1.b07.challenge.body")}</p>
            <div className="number-line-strip" aria-hidden="true">
              <span>1</span><i /><b>√2</b><i /><span>2</span>
            </div>
            <h2 className="q03-prompt">{t("prealgebra.n1.b07.q03.prompt")}</h2>
            {textOptions(IDS.sqrt2, "q03", ["between_1_2", "at_2", "between_2_3"])}
            {feedbackBlock(IDS.sqrt2, "q03")}
          </section>
        )}

        <footer className="lesson-footer trigger-footer">
          <div>
            <span>{t("prealgebra.n1.b07.footerLabel")}</span>
            <p>{t("prealgebra.n1.b07.footerBody")}</p>
          </div>
          <Button size="lg" disabled={!coreResolved || !gridAllResolved} loading={finishing} onClick={onFinish}>
            {lesson.state === "completed" ? t("prealgebra.backToMap") : t("prealgebra.n1.b07.finish")}
          </Button>
        </footer>
      </div>
    </article>
  );
}
