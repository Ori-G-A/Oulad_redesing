import { useState } from "react";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { Button } from "../../../components/ui/Button";
import { LessonFooter } from "./LessonFooter";
import "./ClassifierRigorousLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

const COLS = ["n", "z", "q", "i", "r", "c"] as const;
const ROWS = [
  { value: "minus3", math: "-3", complex: false },
  { value: "zero", math: "0", complex: false },
  { value: "half", math: String.raw`\frac{1}{2}`, complex: false },
  { value: "sqrt2", math: String.raw`\sqrt{2}`, complex: false },
  { value: "pi", math: String.raw`\pi`, complex: false },
  { value: "five", math: "5", complex: false },
  { value: "two_i", math: "2i", complex: true },
  { value: "three_plus_two_i", math: "3 + 2i", complex: true },
] as const;

const rowId = (value: string) => `PREALG-N1-B11-ROW-${value}`;
const descId = (value: string) => `PREALG-N1-B11-DESC-${value}`;
const DESC_OPTIONS = ["pure_imaginary", "complex_non_real"] as const;

export function ClassifierRigorousLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  const showComplex = lesson.explored_complex_branch;
  const cols = showComplex ? COLS : COLS.filter((c) => c !== "c");
  const rows = ROWS.filter((r) => showComplex || !r.complex);

  const restored = lesson.progress.responses;
  const initialMarks: Record<string, Set<string>> = {};
  const initialDesc: Record<string, string> = {};
  const initialResults: Record<string, { feedback: string; correct: boolean }> = {};
  for (const r of rows) {
    const resp = restored[rowId(r.value)];
    const descResp = r.complex ? restored[descId(r.value)] : undefined;
    if (descResp) initialDesc[r.value] = descResp.selected_option;
    if (resp) {
      initialMarks[r.value] = new Set(resp.selected_option.split(",").filter(Boolean));
      const descOk = !r.complex || descResp?.is_expected === true;
      initialResults[r.value] = {
        feedback: resp.is_expected && descOk ? "row_correct" : "",
        correct: resp.is_expected === true && descOk,
      };
    }
  }

  const [marks, setMarks] = useState<Record<string, Set<string>>>(initialMarks);
  const [descMarks, setDescMarks] = useState<Record<string, string>>(initialDesc);
  const [results, setResults] = useState<Record<string, { feedback: string; correct: boolean }>>(initialResults);
  const [attempts, setAttempts] = useState(Object.keys(initialResults).length ? 1 : 0);
  const [verifying, setVerifying] = useState(false);
  const [hintOpen, setHintOpen] = useState(lesson.presentation === "basico");

  const allMarked = rows.every(
    (r) => (marks[r.value]?.size ?? 0) > 0 && (!r.complex || Boolean(descMarks[r.value])),
  );
  const allCorrect = rows.every((r) => results[r.value]?.correct);
  const resolved = allCorrect || attempts >= 2;

  const toggle = (row: string, col: string) => {
    if (resolved || results[row]?.correct) return;
    setMarks((cur) => {
      const next = new Set(cur[row] ?? []);
      if (next.has(col)) next.delete(col);
      else next.add(col);
      return { ...cur, [row]: next };
    });
  };

  const verify = async () => {
    setVerifying(true);
    try {
      const next: Record<string, { feedback: string; correct: boolean }> = {};
      for (const r of rows) {
        if (results[r.value]?.correct) {
          next[r.value] = results[r.value];
          continue;
        }
        const value = COLS.filter((c) => marks[r.value]?.has(c)).join(",");
        const res = await studentApi.lessonInteraction(courseId, lesson.node_id, rowId(r.value), value);
        let correct = res.is_expected === true;
        let feedback = res.feedback_key;
        if (r.complex) {
          const descRes = await studentApi.lessonInteraction(
            courseId, lesson.node_id, descId(r.value), descMarks[r.value],
          );
          // La fila compleja solo es correcta si memberships Y descriptor lo son.
          if (correct && descRes.is_expected !== true) {
            correct = false;
            feedback = descRes.feedback_key;
          }
        }
        next[r.value] = { feedback, correct };
      }
      setResults(next);
      setAttempts((a) => a + 1);
    } finally {
      setVerifying(false);
    }
  };

  return (
    <article className="lesson-page rigorous-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.safeZone")}</span>
      </header>

      <div className="lesson-shell rigorous-shell">
        <header className="rigorous-heading">
          <div>
            <span className="lesson-kicker">{t("prealgebra.n1.b11.kicker")}</span>
            <h1 id="lesson-title">{t("prealgebra.n1.b11.title")}</h1>
            <p>{t(`prealgebra.n1.b11.intro.${lesson.presentation}`)}</p>
          </div>
          <div className="rigorous-katia" aria-label={t("prealgebra.n1.b11.katiaAlt")}>
            <img src="/katia/katIA.png" alt="" aria-hidden="true" />
            <div className="lesson-dialogue">
              <b>KatIA</b>
              <p>{t("prealgebra.n1.b11.katiaMessage")}</p>
            </div>
          </div>
        </header>

        <section className="rigorous-instruction">
          <span>{t("prealgebra.n1.b11.instruction.eyebrow")}</span>
          <p>{t("prealgebra.n1.b11.instruction.body")}</p>
          <div className="rigorous-chain" aria-hidden="true">
            <MathFormula math={String.raw`\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}`} />
          </div>
        </section>

        <section className="rigorous-matrix-wrap" aria-label={t("prealgebra.n1.b11.matrixAria")}>
          <table className="rigorous-matrix">
            <thead>
              <tr>
                <th scope="col"><span className="sr-only">{t("prealgebra.n1.b11.numberCol")}</span></th>
                {cols.map((c) => (
                  <th key={c} scope="col">{t(`prealgebra.n1.b11.cols.${c}`)}</th>
                ))}
                {showComplex && <th scope="col">{t("prealgebra.n1.b11.descriptorCol")}</th>}
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => {
                const result = results[r.value];
                const state = result ? (result.correct ? "ok" : "review") : "";
                return (
                  <tr key={r.value} className={`rigorous-row ${state}`}>
                    <th scope="row" aria-label={t(`prealgebra.n1.b11.aria.${r.value}`)}>
                      <MathFormula math={r.math} />
                    </th>
                    {cols.map((c) => {
                      const checked = marks[r.value]?.has(c) ?? false;
                      return (
                        <td key={c}>
                          <label className="rigorous-cell">
                            <input
                              type="checkbox"
                              checked={checked}
                              disabled={resolved || result?.correct}
                              aria-label={`${t(`prealgebra.n1.b11.aria.${r.value}`)} · ${t(`prealgebra.n1.b11.cols.${c}`)}`}
                              onChange={() => toggle(r.value, c)}
                            />
                          </label>
                        </td>
                      );
                    })}
                    {showComplex && (
                      <td className="rigorous-desc-cell">
                        {r.complex ? (
                          <select
                            value={descMarks[r.value] ?? ""}
                            disabled={resolved || result?.correct}
                            aria-label={`${t(`prealgebra.n1.b11.aria.${r.value}`)} · ${t("prealgebra.n1.b11.descriptorCol")}`}
                            onChange={(e) => setDescMarks((cur) => ({ ...cur, [r.value]: e.target.value }))}
                          >
                            <option value="">{t("prealgebra.n1.b11.descriptorChoose")}</option>
                            {DESC_OPTIONS.map((d) => (
                              <option key={d} value={d}>{t(`prealgebra.n1.b11.descriptor.${d}`)}</option>
                            ))}
                          </select>
                        ) : (
                          <span aria-hidden="true">—</span>
                        )}
                      </td>
                    )}
                  </tr>
                );
              })}
            </tbody>
          </table>
        </section>

        {rows.some((r) => results[r.value]) && (
          <ul className="rigorous-feedback-list">
            {rows.map((r) => {
              const result = results[r.value];
              if (!result) return null;
              return (
                <li key={r.value} className={result.correct ? "ok" : "review"} role="status">
                  <span className="rigorous-feedback-num"><MathFormula math={r.math} /></span>
                  {result.correct
                    ? t("prealgebra.n1.b11.feedback.row_correct")
                    : t(`prealgebra.n1.b11.feedback.${result.feedback}`)}
                </li>
              );
            })}
          </ul>
        )}

        <section className="rigorous-actions">
          <button className="rigorous-hint-toggle" aria-expanded={hintOpen} onClick={() => setHintOpen((o) => !o)}>
            {t("prealgebra.n1.b11.hint.button")}
          </button>
          {!resolved && (
            <Button variant="secondary" disabled={!allMarked} loading={verifying} onClick={verify}>
              {t("prealgebra.n1.b11.verify")}
            </Button>
          )}
        </section>
        {hintOpen && <p className="rigorous-hint">{t("prealgebra.n1.b11.hint.body")}</p>}

        {resolved && (
          <section className="rigorous-closing" role="status">
            <span>{t("prealgebra.n1.b11.closing.eyebrow")}</span>
            <p>{t(`prealgebra.n1.b11.closing.${allCorrect ? "done" : "review"}`)}</p>
          </section>
        )}

        <LessonFooter
          label={t("prealgebra.n1.b11.footerLabel")}
          body={t("prealgebra.n1.b11.footerBody")}
          finishText={t("prealgebra.n1.b11.finish")}
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
