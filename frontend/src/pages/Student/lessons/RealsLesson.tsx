/**
 * lessons/RealsLesson.tsx — Nodo B08 (Reales · ℝ) · cierre de la ruta núcleo
 * ==========================================================================
 * Integra ℕ⊂ℤ⊂ℚ⊂ℝ: los reales son los números de la recta (racionales +
 * irracionales). Q01 conecta la unión; Q02 (selección múltiple) clasifica
 * pertenencia con 2i/3+2i como distractores (complejos, no reales). El reto
 * avanzado recalca que los reales NO son "todos los números posibles".
 * Reutiliza Lesson.css; estilos propios mínimos en RealsLesson.css.
 */
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { Button } from "../../../components/ui/Button";
import { KatiaStorySlot } from "./KatiaStorySlot";
import { LessonFooter } from "./LessonFooter";
import { SetNodeScene } from "./SetNodeScene";
import "./RealsLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

const IDS = {
  union: "PREALG-N1-B08-Q01",
  reals: "PREALG-N1-B08-Q02",
} as const;

const REAL_OPTIONS = ["neg4", "dec075", "sqrt2", "pi", "two_i", "three_plus_two_i"] as const;
const EXPECTED_REALS = ["dec075", "neg4", "pi", "sqrt2"]; // orden sorted
const TRAP = new Set(["two_i", "three_plus_two_i"]);

const OPTION_MATH: Record<string, string> = {
  neg4: "-4",
  dec075: "0{,}75",
  sqrt2: String.raw`\sqrt{2}`,
  pi: String.raw`\pi`,
  two_i: "2i",
  three_plus_two_i: "3+2i",
};

const TF = [
  { key: "s1", expected: "true" },
  { key: "s2", expected: "true" },
  { key: "s3", expected: "true" },
  { key: "s4", expected: "false" },
  { key: "s5", expected: "false" },
] as const;
const tfId = (key: string) => `PREALG-N1-B08-${key.toUpperCase()}`;

function tfFeedback(key: string, selected: string): string {
  const item = TF.find((i) => i.key === key);
  if (item && selected === item.expected) return "tf_correct";
  if (key === "s3") return "irrational_is_real_false";
  if (key === "s4") return "real_is_rational_true";
  if (key === "s5") return "complex_in_real_line";
  return "tf_review";
}

function unionFeedback(option: string): string {
  return {
    union_yes: "union_correct",
    irr_not_on_line: "irr_are_on_line",
    integers_left_out: "integers_included",
  }[option] as string;
}

/** Reconstruye el feedback de Q02 al restaurar progreso (mismo orden que el backend). */
function realsFeedback(csv: string, isExpected: boolean | null): string {
  if (isExpected) return "reales_correct";
  const selected = new Set(csv.split(",").filter(Boolean));
  if ([...selected].some((o) => TRAP.has(o))) return "complex_not_real";
  if (EXPECTED_REALS.some((o) => !selected.has(o))) return "irrationals_are_real";
  return "reales_review";
}

export function RealsLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  const restored = lesson.progress.responses;
  const [answers, setAnswers] = useState<Record<string, string>>(
    Object.fromEntries(Object.entries(restored).map(([id, r]) => [id, r.selected_option])),
  );
  const [attempts, setAttempts] = useState<Record<string, number>>(
    Object.fromEntries(Object.entries(restored).map(([id, r]) => [id, r.is_expected ? 2 : 1])),
  );
  const [feedback, setFeedback] = useState<Record<string, string>>(
    Object.fromEntries(
      Object.entries(restored).map(([id, r]) => [
        id,
        id === IDS.union
          ? unionFeedback(r.selected_option)
          : id === IDS.reals
            ? realsFeedback(r.selected_option, r.is_expected)
            : tfFeedback(id.replace("PREALG-N1-B08-", "").toLowerCase(), r.selected_option),
      ]),
    ),
  );
  const [picks, setPicks] = useState<Set<string>>(
    new Set((restored[IDS.reals]?.selected_option ?? "").split(",").filter(Boolean)),
  );
  const [challenge, setChallenge] = useState("");

  const mutation = useMutation({
    mutationFn: ({ id, option }: { id: string; option: string }) =>
      studentApi.lessonInteraction(courseId, lesson.node_id, id, option),
    onSuccess: (result) => {
      setAnswers((c) => ({ ...c, [result.interaction_id]: result.selected_option }));
      setAttempts((c) => ({ ...c, [result.interaction_id]: (c[result.interaction_id] ?? 0) + 1 }));
      setFeedback((c) => ({ ...c, [result.interaction_id]: result.feedback_key }));
    },
  });

  const unionCorrect = answers[IDS.union] === "union_yes";
  const realsCorrect = () => {
    const csv = answers[IDS.reals];
    return Boolean(csv) && csv.split(",").sort().join(",") === EXPECTED_REALS.join(",");
  };
  const resolved = (id: string, isCorrect: boolean) => isCorrect || (attempts[id] ?? 0) >= 2;
  const unionResolved = resolved(IDS.union, unionCorrect);
  const realsResolved = resolved(IDS.reals, realsCorrect());
  const tfCorrect = (key: string) => answers[tfId(key)] === TF.find((i) => i.key === key)!.expected;
  const tfResolved = (key: string) => resolved(tfId(key), tfCorrect(key));
  const tfAllResolved = TF.every((i) => tfResolved(i.key));
  const allResolved = unionResolved && realsResolved && tfAllResolved;
  const isAdvanced = lesson.presentation === "avanzado";

  const submit = (id: string, option: string) => mutation.mutate({ id, option });
  const toggle = (option: string) => {
    if (realsResolved) return;
    setPicks((current) => {
      const next = new Set(current);
      if (next.has(option)) next.delete(option);
      else next.add(option);
      return next;
    });
  };
  const picksValue = REAL_OPTIONS.filter((o) => picks.has(o)).slice().sort().join(",");

  const feedbackBlock = (id: string, isCorrect: boolean, revealKey: string) => {
    if (!feedback[id]) return null;
    const done = resolved(id, isCorrect);
    return (
      <div className="trigger-feedback" role="status">
        <p>{t(`prealgebra.n1.b08.feedback.${feedback[id]}`)}</p>
        {!done && <strong>{t("prealgebra.n1.b08.feedback.retry")}</strong>}
        {!isCorrect && done && <strong>{t(`prealgebra.n1.b08.feedback.reveal.${revealKey}`)}</strong>}
      </div>
    );
  };

  return (
    <article className="lesson-page reals-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.safeZone")}</span>
      </header>

      <div className="lesson-shell">
        <header className="trigger-heading">
          <span className="lesson-kicker">{t("prealgebra.n1.b08.kicker")}</span>
          <h1 id="lesson-title">{t("prealgebra.n1.b08.title")}</h1>
          <p>{t(`prealgebra.n1.b08.intro.${lesson.presentation}`)}</p>
        </header>

        {/* Diagrama de inclusión integrado: rótulos dentro de cada zona anidada. */}
        <SetNodeScene
          imageSrc="/prealgebra/step-reales.png"
          activeStep="reals"
          ariaLabel={t("prealgebra.n1.b08.diagramAria")}
        />

        <KatiaStorySlot
          eyebrow={t("prealgebra.n1.b08.story.katiaEyebrow")}
          title={t("prealgebra.n1.b08.story.katiaTitle")}
          body={t("prealgebra.n1.b08.story.katiaBody")}
          question={t("prealgebra.n1.b08.story.katiaQuestion")}
          imageSrc="/prealgebra/generated/n1-agora/b08-reales-v4.png"
        />

        <section className="set-story" aria-label={t("prealgebra.n1.b08.story.label")}>
          <article>
            <span>{t("prealgebra.n1.b08.story.discoveryEyebrow")}</span>
            <h2>{t("prealgebra.n1.b08.story.discoveryTitle")}</h2>
            <p>{t("prealgebra.n1.b08.story.discoveryBody")}</p>
          </article>
          <article className="set-formal">
            <span>{t("prealgebra.n1.b08.story.definitionEyebrow")}</span>
            <h2>{t("prealgebra.n1.b08.story.definitionTitle")}</h2>
            <MathFormula math={String.raw`\mathbb{R}=\mathbb{Q}\cup(\mathbb{R}\setminus\mathbb{Q})`} />
            <p>{t("prealgebra.n1.b08.story.definitionBody")}</p>
          </article>
        </section>

        <section className="set-base-examples set-examples-standalone" aria-label={t("prealgebra.n1.b08.story.examplesLabel")}>
          {(["rational", "irrational", "trap"] as const).map((example) => (
            <article key={example}>
              <span>{t(`prealgebra.n1.b08.story.examples.${example}.eyebrow`)}</span>
              <h3>{t(`prealgebra.n1.b08.story.examples.${example}.title`)}</h3>
              <p>{t(`prealgebra.n1.b08.story.examples.${example}.body`)}</p>
              <ol>
                {[0, 1, 2].map((step) => (
                  <li key={step}>{t(`prealgebra.n1.b08.story.examples.${example}.steps.${step}`)}</li>
                ))}
              </ol>
            </article>
          ))}
        </section>

        <section className="real-line-showcase" aria-label="Recta real con racionales e irracionales">
          <div className="real-line-track" aria-hidden="true">
            <span style={{ left: "8%" }}>-3</span>
            <span style={{ left: "39%" }}>0</span>
            <span style={{ left: "49%" }}>1/2</span>
            <span style={{ left: "61%" }}>√2</span>
            <span style={{ left: "84%" }}>π</span>
          </div>
          <div>
            <span>Recta real</span>
            <h2>Una sola línea, muchos tipos de número</h2>
            <p>Los racionales y los irracionales ocupan posiciones en la recta. Por eso todos ellos pertenecen a los reales, aunque no todos pertenezcan al mismo subconjunto.</p>
          </div>
        </section>

        <section className="inclusion-diagram real-union-diagram" aria-label={t("prealgebra.n1.b08.diagramAria")}>
          <div className="real-set-shell">
            <span className="set-diagram-label real-label">
              <MathFormula math={String.raw`\mathbb{R}`} /> {t("prealgebra.n1.b08.zones.reals")}
            </span>
            <div className="real-union-grid">
              <div className="real-q-region">
                <span className="set-diagram-label">
                  <MathFormula math={String.raw`\mathbb{Q}`} /> {t("prealgebra.n1.b08.zones.rationals")}
                </span>
                <div className="real-z-region">
                  <span className="set-diagram-label">
                    <MathFormula math={String.raw`\mathbb{Z}`} /> {t("prealgebra.n1.b08.zones.integers")}
                  </span>
                  <div className="real-n-region">
                    <span className="set-diagram-label">
                      <MathFormula math={String.raw`\mathbb{N}`} /> {t("prealgebra.n1.b08.zones.naturals")}
                    </span>
                    <div className="set-example-row">
                      <MathFormula math="1" />
                      <MathFormula math="2" />
                      <MathFormula math="5" />
                    </div>
                  </div>
                  <div className="set-example-row muted">
                    <MathFormula math="-4" />
                    <MathFormula math="-1" />
                    <MathFormula math="0" />
                  </div>
                </div>
                <div className="set-example-row q-examples">
                  <MathFormula math={String.raw`-\frac{3}{7}`} />
                  <MathFormula math={String.raw`\frac{1}{2}`} />
                  <MathFormula math="0{,}4" />
                </div>
              </div>
              <div className="real-irr-region">
                <span className="set-diagram-label">
                  <MathFormula math={String.raw`\mathbb{R}\setminus\mathbb{Q}`} /> {t("prealgebra.n1.b08.zones.irrationals")}
                </span>
                <div className="set-example-column">
                  <MathFormula math={String.raw`\sqrt{2}`} />
                  <MathFormula math={String.raw`\pi`} />
                  <MathFormula math="e" />
                  <MathFormula math={String.raw`-3{,}010010001\ldots`} />
                </div>
              </div>
            </div>
            <div className="real-union-note">
              <MathFormula math={String.raw`\mathbb{R}=\mathbb{Q}\cup(\mathbb{R}\setminus\mathbb{Q})`} />
            </div>
          </div>
        </section>

        <section aria-label={t("prealgebra.n1.b08.practiceLabel")}>
          <article className="trigger-question">
            <span className="question-number">01</span>
            <div>
              <h2>{t("prealgebra.n1.b08.q01.prompt")}</h2>
              <div className="choice-stack">
                {(["union_yes", "irr_not_on_line", "integers_left_out"] as const).map((option) => (
                  <button
                    key={option}
                    className={answers[IDS.union] === option ? "selected" : ""}
                    disabled={unionResolved || mutation.isPending}
                    aria-pressed={answers[IDS.union] === option}
                    onClick={() => submit(IDS.union, option)}
                  >
                    {t(`prealgebra.n1.b08.q01.options.${option}`)}
                  </button>
                ))}
              </div>
              {feedbackBlock(IDS.union, unionCorrect, "q01")}
            </div>
          </article>

          <article className="trigger-question">
            <span className="question-number">02</span>
            <div>
              <h2>{t("prealgebra.n1.b08.q02.prompt")}</h2>
              <div className="real-choices" role="group" aria-label={t("prealgebra.n1.b08.q02.groupAria")}>
                {REAL_OPTIONS.map((option) => (
                  <button
                    key={option}
                    className={picks.has(option) ? "selected" : ""}
                    disabled={realsResolved}
                    aria-pressed={picks.has(option)}
                    aria-label={t(`prealgebra.n1.b08.q02.aria.${option}`)}
                    onClick={() => toggle(option)}
                  >
                    <MathFormula math={OPTION_MATH[option]} />
                  </button>
                ))}
              </div>
              <Button
                variant="secondary"
                disabled={!picksValue || realsResolved}
                loading={mutation.isPending}
                onClick={() => submit(IDS.reals, picksValue)}
              >
                {t("prealgebra.n1.b08.checkSelection")}
              </Button>
              {feedbackBlock(IDS.reals, realsCorrect(), "q02")}
            </div>
          </article>
        </section>

        <section className="reals-tf" aria-label={t("prealgebra.n1.b08.tf.label")}>
          <h2>{t("prealgebra.n1.b08.tf.prompt")}</h2>
          {TF.map((item) => {
            const id = tfId(item.key);
            const done = tfResolved(item.key);
            return (
              <div className="tf-row" key={item.key}>
                <p className="tf-statement">{t(`prealgebra.n1.b08.tf.items.${item.key}`)}</p>
                <div className="choice-row" role="group" aria-label={t(`prealgebra.n1.b08.tf.items.${item.key}`)}>
                  {(["true", "false"] as const).map((option) => (
                    <button
                      key={option}
                      className={answers[id] === option ? "selected" : ""}
                      disabled={done || mutation.isPending}
                      aria-pressed={answers[id] === option}
                      onClick={() => submit(id, option)}
                    >
                      {t(`prealgebra.n1.b08.tf.${option}`)}
                    </button>
                  ))}
                </div>
                {feedback[id] && (
                  <p className={`trigger-feedback ${tfCorrect(item.key) ? "ok" : done ? "review" : ""}`} role="status">
                    {t(`prealgebra.n1.b08.tf.feedback.${feedback[id]}`)}
                  </p>
                )}
              </div>
            );
          })}
        </section>

        {allResolved && isAdvanced && (
          <section className="trigger-challenge">
            <span>{t("prealgebra.n1.b08.challenge.eyebrow")}</span>
            <h2>{t("prealgebra.n1.b08.challenge.title")}</h2>
            <div className="choice-row">
              {(["beyond", "all"] as const).map((option) => (
                <button
                  key={option}
                  className={challenge === option ? "selected" : ""}
                  disabled={Boolean(challenge)}
                  onClick={() => setChallenge(option)}
                >
                  {t(`prealgebra.n1.b08.challenge.options.${option}`)}
                </button>
              ))}
            </div>
            {challenge && (
              <p className="trigger-feedback" role="status">
                {t(`prealgebra.n1.b08.challenge.feedback.${challenge}`)}
              </p>
            )}
          </section>
        )}

        <LessonFooter
          label={t("prealgebra.n1.b08.footerLabel")}
          body={t("prealgebra.n1.b08.footerBody")}
          finishText={t("prealgebra.n1.b08.finish")}
          completed={lesson.state === "completed"}
          canFinish={allResolved}
          finishing={finishing}
          onFinish={onFinish}
          onBack={onBack}
        />
      </div>
    </article>
  );
}
