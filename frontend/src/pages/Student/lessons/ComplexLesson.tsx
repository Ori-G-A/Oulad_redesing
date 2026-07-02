import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail, type LessonInteractionResult } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { KatiaStorySlot } from "./KatiaStorySlot";
import { LessonFooter } from "./LessonFooter";
import "./ComplexLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

// Las dos interacciones graduadas ya existen en el catálogo backend (B09).
// El reconocimiento de la unidad imaginaria se presenta como contenido (Katia).
const IDS = {
  recognize: "PREALG-N1-B09-Q03",
  parts: "PREALG-N1-B09-Q01",
  plane: "PREALG-N1-B09-Q02",
} as const;

const QR_OPTIONS = ["imaginary_unit", "irrationals", "natural", "zero"] as const;
const Q01_OPTIONS = ["re3_im2", "re2_im3", "re0_im5", "no_real"] as const;
const Q02_OPTIONS = ["plane_off_line", "on_real_line", "cannot_place", "real_axis_5"] as const;

const EXPECTED: Record<string, string> = {
  [IDS.recognize]: "imaginary_unit",
  [IDS.parts]: "re3_im2",
  [IDS.plane]: "plane_off_line",
};

function restoredFeedback(id: string, selected: string): string {
  if (id === IDS.recognize) {
    return { imaginary_unit: "recognize_correct", irrationals: "notation_warning", natural: "not_those_sets", zero: "not_those_sets" }[selected] ?? "";
  }
  if (id === IDS.parts) {
    return { re3_im2: "parts_correct", re2_im3: "parts_swapped", re0_im5: "not_zero_five", no_real: "has_real_part" }[selected] ?? "";
  }
  return { plane_off_line: "plane_correct", on_real_line: "not_on_line", cannot_place: "can_place_in_plane", real_axis_5: "not_at_5" }[selected] ?? "";
}

export function ComplexLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  const restored = lesson.progress.responses;
  const initialAnswers = Object.fromEntries(
    Object.entries(restored).map(([id, r]) => [id, r.selected_option]),
  );
  const initialAttempts = Object.fromEntries(
    Object.entries(restored).map(([id, r]) => [id, r.is_expected ? 2 : 1]),
  );
  const initialFeedback = Object.fromEntries(
    Object.entries(restored).map(([id, r]) => [id, restoredFeedback(id, r.selected_option)]),
  );

  const [answers, setAnswers] = useState<Record<string, string>>(initialAnswers);
  const [attempts, setAttempts] = useState<Record<string, number>>(initialAttempts);
  const [feedback, setFeedback] = useState<Record<string, string>>(initialFeedback);

  const mutation = useMutation({
    mutationFn: ({ id, option }: { id: string; option: string }) =>
      studentApi.lessonInteraction(courseId, lesson.node_id, id, option),
    onSuccess: (result: LessonInteractionResult) => {
      setAnswers((c) => ({ ...c, [result.interaction_id]: result.selected_option }));
      setAttempts((c) => ({ ...c, [result.interaction_id]: (c[result.interaction_id] ?? 0) + 1 }));
      setFeedback((c) => ({ ...c, [result.interaction_id]: result.feedback_key }));
    },
  });

  const isCorrect = (id: string) => answers[id] === EXPECTED[id];
  const resolved = (id: string) => isCorrect(id) || (attempts[id] ?? 0) >= 2;
  const allResolved = Object.values(IDS).every(resolved);
  const submit = (id: string, option: string) => mutation.mutate({ id, option });

  const feedbackBlock = (id: string, answerKey: string) => {
    if (!feedback[id]) return null;
    const shouldReveal = !isCorrect(id) && (attempts[id] ?? 0) >= 2;
    return (
      <div className="trigger-feedback" role="status">
        <p>{t(`prealgebra.n1.b09.feedback.${feedback[id]}`)}</p>
        {!resolved(id) && <strong>{t("prealgebra.n1.b09.feedback.retry")}</strong>}
        {shouldReveal && <strong>{t(`prealgebra.n1.b09.feedback.reveal.${answerKey}`)}</strong>}
      </div>
    );
  };

  const renderChoices = (id: string, options: readonly string[]) => (
    <div className="choice-stack">
      {options.map((option) => (
        <button
          key={option}
          className={answers[id] === option ? "selected" : ""}
          disabled={resolved(id) || mutation.isPending}
          aria-pressed={answers[id] === option}
          onClick={() => submit(id, option)}
        >
          {t(`prealgebra.n1.b09.${id === IDS.parts ? "q01" : id === IDS.plane ? "q02" : "q03"}.options.${option}`)}
        </button>
      ))}
    </div>
  );

  return (
    <article className="lesson-page complex-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.optionalBranch")}</span>
      </header>

      <div className="lesson-shell complex-shell">
        <header className="complex-heading">
          <span className="lesson-kicker">{t("prealgebra.n1.b09.kicker")}</span>
          <h1 id="lesson-title">{t("prealgebra.n1.b09.title")}</h1>
          <p>{t(`prealgebra.n1.b09.intro.${lesson.presentation}`)}</p>
        </header>

        <figure className="complex-step-scene" aria-label="Escalón visual de los números complejos">
          <img src="/prealgebra/step-complejos.png" alt="" aria-hidden="true" loading="lazy" />
        </figure>

        <KatiaStorySlot
          eyebrow={t("prealgebra.n1.b09.story.katiaEyebrow")}
          title={t("prealgebra.n1.b09.story.katiaTitle")}
          body={t("prealgebra.n1.b09.story.katiaBody")}
          question={t("prealgebra.n1.b09.story.katiaQuestion")}
        />

        <section className="set-story" aria-label={t("prealgebra.n1.b09.story.label")}>
          <article>
            <span>{t("prealgebra.n1.b09.story.discoveryEyebrow")}</span>
            <h2>{t("prealgebra.n1.b09.story.discoveryTitle")}</h2>
            <p>{t("prealgebra.n1.b09.story.discoveryBody")}</p>
            <div className="complex-formula" aria-label={t("prealgebra.n1.b09.story.unitAria")}>
              <MathFormula math={String.raw`i^{2}=-1`} />
            </div>
          </article>
          <article className="set-formal">
            <span>{t("prealgebra.n1.b09.story.definitionEyebrow")}</span>
            <h2>{t("prealgebra.n1.b09.story.definitionTitle")}</h2>
            <MathFormula math={String.raw`z=a+bi,\quad a,b\in\mathbb{R}`} />
            <p>{t("prealgebra.n1.b09.story.definitionBody")}</p>
          </article>
        </section>

        <section className="set-base-examples set-examples-standalone" aria-label={t("prealgebra.n1.b09.story.examplesLabel")}>
          {(["parts", "real", "trap"] as const).map((example) => (
            <article key={example}>
              <span>{t(`prealgebra.n1.b09.story.examples.${example}.eyebrow`)}</span>
              <h3>{t(`prealgebra.n1.b09.story.examples.${example}.title`)}</h3>
              <p>{t(`prealgebra.n1.b09.story.examples.${example}.body`)}</p>
              <ol>
                {[0, 1, 2].map((step) => (
                  <li key={step}>{t(`prealgebra.n1.b09.story.examples.${example}.steps.${step}`)}</li>
                ))}
              </ol>
            </article>
          ))}
        </section>

        <section className="complex-set-diagram" aria-label="Diagrama de conjuntos de los números complejos">
          <div className="complex-set-shell">
            <span className="set-diagram-label complex-label">
              <MathFormula math={String.raw`\mathbb{C}`} /> Complejos
            </span>
            <div className="complex-set-grid">
              <div className="complex-real-region">
                <span className="set-diagram-label">
                  <MathFormula math={String.raw`\mathbb{R}`} /> Reales
                </span>
                <div className="complex-real-union">
                  <div>
                    <span className="set-diagram-label">
                      <MathFormula math={String.raw`\mathbb{Q}`} /> Racionales
                    </span>
                    <div className="set-example-row">
                      <MathFormula math="-4" />
                      <MathFormula math={String.raw`\frac{1}{2}`} />
                      <MathFormula math="0{,}75" />
                    </div>
                  </div>
                  <div>
                    <span className="set-diagram-label">
                      <MathFormula math={String.raw`\mathbb{R}\setminus\mathbb{Q}`} /> Irracionales
                    </span>
                    <div className="set-example-row">
                      <MathFormula math={String.raw`\sqrt{2}`} />
                      <MathFormula math={String.raw`\pi`} />
                    </div>
                  </div>
                </div>
              </div>
              <div className="complex-nonreal-region">
                <span className="set-diagram-label">
                  <MathFormula math={String.raw`\mathbb{C}\setminus\mathbb{R}`} /> Complejos no reales
                </span>
                <div className="set-example-column">
                  <MathFormula math="2i" />
                  <MathFormula math="3+2i" />
                  <MathFormula math="-1+i" />
                </div>
              </div>
            </div>
            <div className="complex-union-note">
              <MathFormula math={String.raw`\mathbb{C}=\mathbb{R}\cup(\mathbb{C}\setminus\mathbb{R})`} />
            </div>
          </div>
        </section>

        <section className="complex-practice" aria-label={t("prealgebra.n1.b09.practiceLabel")}>
          <article className="complex-question">
            <span className="question-number">01</span>
            <div>
              <h2>{t("prealgebra.n1.b09.q03.prompt")}</h2>
              <div className="complex-sample" aria-hidden="true"><MathFormula math={String.raw`i^{2}=-1`} /></div>
              {renderChoices(IDS.recognize, QR_OPTIONS)}
              {feedbackBlock(IDS.recognize, "q03")}
            </div>
          </article>

          <article className="complex-question">
            <span className="question-number">02</span>
            <div>
              <h2>{t("prealgebra.n1.b09.q01.prompt")}</h2>
              <div className="complex-sample" aria-hidden="true"><MathFormula math={String.raw`3+2i`} /></div>
              {renderChoices(IDS.parts, Q01_OPTIONS)}
              {feedbackBlock(IDS.parts, "q01")}
            </div>
          </article>

          <article className="complex-question">
            <span className="question-number">03</span>
            <div>
              <h2>{t("prealgebra.n1.b09.q02.prompt")}</h2>
              {renderChoices(IDS.plane, Q02_OPTIONS)}
              {feedbackBlock(IDS.plane, "q02")}
            </div>
          </article>
        </section>

        <LessonFooter
          label={t("prealgebra.n1.b09.footerLabel")}
          body={t("prealgebra.n1.b09.footerBody")}
          finishText={t("prealgebra.n1.b09.finish")}
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
