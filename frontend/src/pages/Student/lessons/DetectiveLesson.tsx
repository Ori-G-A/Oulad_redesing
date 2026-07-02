import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";
import { studentApi, type LessonDetail } from "../../../api/student";
import { MathFormula } from "../../../components/Math/MathContent";
import { LessonFooter } from "./LessonFooter";
import "./DetectiveLesson.css";

type Props = {
  lesson: LessonDetail;
  courseId: string;
  onBack: () => void;
  onFinish: () => Promise<void>;
  finishing: boolean;
};

const STATEMENTS = [
  { key: "a1", expected: "true", complex: false },
  { key: "a2", expected: "false", complex: false },
  { key: "a3", expected: "true", complex: false },
  { key: "a4", expected: "true", complex: false },
  { key: "a5", expected: "false", complex: false },
  { key: "a6", expected: "false", complex: false },
  { key: "a7", expected: "true", complex: false },
  { key: "a8", expected: "false", complex: false },
  { key: "a9", expected: "true", complex: false },
  { key: "a10", expected: "true", complex: true },
  { key: "a11", expected: "false", complex: true },
  { key: "a12", expected: "false", complex: true },
  { key: "a13", expected: "true", complex: true },
  { key: "a14", expected: "true", complex: true },
] as const;

const stmtId = (key: string) => `PREALG-N1-B12-${key.toUpperCase()}`;

export function DetectiveLesson({ lesson, courseId, onBack, onFinish, finishing }: Props) {
  const { t } = useTranslation();
  const statements = STATEMENTS.filter((s) => lesson.explored_complex_branch || !s.complex);

  const restored = lesson.progress.responses;
  const fbFor = (key: string, isExpected: boolean | null) => `${key}_${isExpected ? "correct" : "incorrect"}`;

  const [answers, setAnswers] = useState<Record<string, string>>(
    Object.fromEntries(Object.entries(restored).map(([id, r]) => [id, r.selected_option])),
  );
  const [attempts, setAttempts] = useState<Record<string, number>>(
    Object.fromEntries(Object.entries(restored).map(([id, r]) => [id, r.is_expected ? 2 : 1])),
  );
  const [feedback, setFeedback] = useState<Record<string, string>>(
    Object.fromEntries(
      Object.entries(restored).map(([id, r]) => [id, fbFor(id.replace("PREALG-N1-B12-", "").toLowerCase(), r.is_expected)]),
    ),
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

  const correct = (s: { key: string; expected: string }) => answers[stmtId(s.key)] === s.expected;
  const resolved = (s: { key: string; expected: string }) => correct(s) || (attempts[stmtId(s.key)] ?? 0) >= 2;
  const allResolved = statements.every(resolved);
  const submit = (id: string, option: string) => mutation.mutate({ id, option });

  return (
    <article className="lesson-page detective-page" aria-labelledby="lesson-title">
      <header className="lesson-topbar">
        <button className="lesson-back" onClick={onBack}>{t("prealgebra.backToMap")}</button>
        <span className="lesson-safe">{t("prealgebra.safeZone")}</span>
      </header>

      <div className="lesson-shell detective-shell">
        <header className="detective-heading">
          <div>
            <span className="lesson-kicker">{t("prealgebra.n1.b12.kicker")}</span>
            <h1 id="lesson-title">{t("prealgebra.n1.b12.title")}</h1>
            <p>{t(`prealgebra.n1.b12.intro.${lesson.presentation}`)}</p>
          </div>
          <div className="detective-katia" aria-label={t("prealgebra.n1.b12.katiaAlt")}>
            <img src="/katia/katIA.png" alt="" aria-hidden="true" />
            <div className="lesson-dialogue">
              <b>KatIA</b>
              <p>{t("prealgebra.n1.b12.katiaMessage")}</p>
            </div>
          </div>
        </header>

        <section className="detective-reminder">
          <span>{t("prealgebra.n1.b12.instruction.eyebrow")}</span>
          <p>{t("prealgebra.n1.b12.instruction.body")}</p>
          <div className="detective-chain" aria-label={t("prealgebra.n1.b12.reminderAria")}>
            <MathFormula math={String.raw`\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}`} />
          </div>
        </section>

        <ol className="detective-list">
          {statements.map((s, index) => {
            const id = stmtId(s.key);
            const done = resolved(s);
            return (
              <li key={s.key} className="detective-row">
                <span className="detective-num" aria-hidden="true">{String(index + 1).padStart(2, "0")}</span>
                <div className="detective-body">
                  <p className="detective-statement">{t(`prealgebra.n1.b12.statements.${s.key}`)}</p>
                  <div className="choice-row" role="group" aria-label={t(`prealgebra.n1.b12.statements.${s.key}`)}>
                    {(["true", "false"] as const).map((option) => (
                      <button
                        key={option}
                        className={answers[id] === option ? "selected" : ""}
                        disabled={done || mutation.isPending}
                        aria-pressed={answers[id] === option}
                        onClick={() => submit(id, option)}
                      >
                        {t(`prealgebra.n1.b12.${option}`)}
                      </button>
                    ))}
                  </div>
                  {feedback[id] && (
                    <p className={`trigger-feedback ${correct(s) ? "ok" : done ? "review" : ""}`} role="status">
                      {t(`prealgebra.n1.b12.feedback.${feedback[id]}`)}
                      {!done && <strong> {t("prealgebra.n1.b12.feedback.retry")}</strong>}
                    </p>
                  )}
                </div>
              </li>
            );
          })}
        </ol>

        <LessonFooter
          label={t("prealgebra.n1.b12.footerLabel")}
          body={t("prealgebra.n1.b12.footerBody")}
          finishText={t("prealgebra.n1.b12.finish")}
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
