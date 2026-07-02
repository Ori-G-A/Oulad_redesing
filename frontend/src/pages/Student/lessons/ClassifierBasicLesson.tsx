import { useState } from "react";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { Button } from "../../../components/ui/Button";
import { LessonFooter } from "./LessonFooter";
import "./ClassifierBasicLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

const ZONES = ["naturals", "integers", "rationals", "irrationals", "pure_imaginary", "complex_general"] as const;
const REAL_ZONES = ["naturals", "integers", "rationals", "irrationals"] as const;

// value → KaTeX label · requiresComplex · avanzado-only
const CARDS = [
  { value: "minus3", math: "-3", complex: false, avanzado: false },
  { value: "zero", math: "0", complex: false, avanzado: false },
  { value: "half", math: String.raw`\frac{1}{2}`, complex: false, avanzado: false },
  { value: "sqrt2", math: String.raw`\sqrt{2}`, complex: false, avanzado: false },
  { value: "pi", math: String.raw`\pi`, complex: false, avanzado: false },
  { value: "five", math: "5", complex: false, avanzado: false },
  { value: "two_i", math: "2i", complex: true, avanzado: false },
  { value: "three_plus_two_i", math: "3 + 2i", complex: true, avanzado: false },
  { value: "decimal_0333", math: String.raw`0{,}\overline{3}`, complex: false, avanzado: true },
  { value: "neg7", math: "-7", complex: false, avanzado: true },
  { value: "four_fourths", math: String.raw`\frac{4}{4}`, complex: false, avanzado: true },
] as const;

const cardId = (value: string) => `PREALG-N1-B10-CARD-${value}`;

export function ClassifierBasicLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  // Cascada: las tarjetas/zonas complejas solo si el estudiante exploró B09
  // (no por banda) — decisión bloqueada del nivel.
  const showComplex = lesson.explored_complex_branch;
  const isAvanzado = lesson.presentation === "avanzado";
  const cards = CARDS.filter((c) => (showComplex || !c.complex) && (isAvanzado || !c.avanzado));
  const zones = showComplex ? ZONES : REAL_ZONES;
  const hintAlwaysVisible = lesson.presentation === "basico";

  const restored = lesson.progress.responses;
  const initialAssign: Record<string, string> = {};
  const initialResults: Record<string, { feedback: string; correct: boolean }> = {};
  for (const c of cards) {
    const r = restored[cardId(c.value)];
    if (r) {
      initialAssign[c.value] = r.selected_option;
      // El backend solo persiste selección + is_expected; al restaurar marcamos
      // correcto/revisar sin recomputar la clave específica (se regenera al reverificar).
      initialResults[c.value] = { feedback: r.is_expected ? "card_correct" : "", correct: r.is_expected === true };
    }
  }

  const [assign, setAssign] = useState<Record<string, string>>(initialAssign);
  const [results, setResults] = useState<Record<string, { feedback: string; correct: boolean }>>(initialResults);
  const [attempts, setAttempts] = useState(Object.keys(initialResults).length ? 1 : 0);
  const [verifying, setVerifying] = useState(false);
  const [hintOpen, setHintOpen] = useState(hintAlwaysVisible);

  const allAssigned = cards.every((c) => assign[c.value]);
  const allCorrect = cards.every((c) => results[c.value]?.correct);
  const resolved = allCorrect || attempts >= 2;

  const verify = async () => {
    setVerifying(true);
    try {
      const next: Record<string, { feedback: string; correct: boolean }> = {};
      for (const c of cards) {
        const zone = assign[c.value];
        if (results[c.value]?.correct) {
          next[c.value] = results[c.value];
          continue;
        }
        const res = await studentApi.lessonInteraction(courseId, lesson.node_id, cardId(c.value), zone);
        next[c.value] = { feedback: res.feedback_key, correct: res.is_expected === true };
      }
      setResults(next);
      setAttempts((a) => a + 1);
    } finally {
      setVerifying(false);
    }
  };

  return (
    <article className="lesson-page classifier-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.safeZone")}</span>
      </header>

      <div className="lesson-shell classifier-shell">
        <header className="classifier-heading">
          <div>
            <span className="lesson-kicker">{t("prealgebra.n1.b10.kicker")}</span>
            <h1 id="lesson-title">{t("prealgebra.n1.b10.title")}</h1>
            <p>{t(`prealgebra.n1.b10.intro.${lesson.presentation}`)}</p>
          </div>
          <div className="classifier-katia" aria-label={t("prealgebra.n1.b10.katiaAlt")}>
            <img src="/katia/katIA.png" alt="" aria-hidden="true" />
            <div className="lesson-dialogue">
              <b>KatIA</b>
              <p>{t("prealgebra.n1.b10.katiaMessage")}</p>
            </div>
          </div>
        </header>

        <section className="classifier-instruction">
          <span>{t("prealgebra.n1.b10.instruction.eyebrow")}</span>
          <p>{t("prealgebra.n1.b10.instruction.body")}</p>
          <small>{t("prealgebra.n1.b10.instruction.note")}</small>
        </section>

        <section className="classifier-board" aria-label={t("prealgebra.n1.b10.boardAria")}>
          {cards.map((c) => {
            const result = results[c.value];
            const state = result ? (result.correct ? "ok" : "review") : "";
            return (
              <article className={`classify-card ${state}`} key={c.value}>
                <div className="classify-number" aria-label={t(`prealgebra.n1.b10.aria.${c.value}`)}>
                  <MathFormula math={c.math} />
                </div>
                <label className="classify-pick">
                  <span className="sr-only">{t("prealgebra.n1.b10.pickAria")}</span>
                  <select
                    value={assign[c.value] ?? ""}
                    disabled={resolved || result?.correct}
                    onChange={(e) => setAssign((cur) => ({ ...cur, [c.value]: e.target.value }))}
                  >
                    <option value="">{t("prealgebra.n1.b10.choose")}</option>
                    {zones.map((z) => (
                      <option key={z} value={z}>{t(`prealgebra.n1.b10.zones.${z}`)}</option>
                    ))}
                  </select>
                </label>
                {result && (
                  <p className={`classify-feedback ${state}`} role="status">
                    {result.correct
                      ? t("prealgebra.n1.b10.feedback.card_correct")
                      : t(`prealgebra.n1.b10.feedback.${result.feedback}`)}
                  </p>
                )}
              </article>
            );
          })}
        </section>

        <section className="classifier-actions">
          <button
            className="classifier-hint-toggle"
            aria-expanded={hintOpen}
            onClick={() => setHintOpen((o) => !o)}
          >
            {t("prealgebra.n1.b10.hint.button")}
          </button>
          {!resolved && (
            <Button variant="secondary" disabled={!allAssigned} loading={verifying} onClick={verify}>
              {t("prealgebra.n1.b10.verify")}
            </Button>
          )}
        </section>
        {hintOpen && <p className="classifier-hint">{t("prealgebra.n1.b10.hint.body")}</p>}

        {resolved && (
          <section className="classifier-closing" role="status">
            <span>{t("prealgebra.n1.b10.closing.eyebrow")}</span>
            <p>{t(`prealgebra.n1.b10.closing.${allCorrect ? "done" : "review"}`)}</p>
          </section>
        )}

        <LessonFooter
          label={t("prealgebra.n1.b10.footerLabel")}
          body={t("prealgebra.n1.b10.footerBody")}
          finishText={t("prealgebra.n1.b10.finish")}
          completed={lesson.state === "completed"}
          canFinish={resolved}
          finishing={finishing}
          onFinish={onFinish}
          onBack={onBack}
        />
      </div>
    </article>
  );
}
