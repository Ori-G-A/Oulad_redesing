import { Fragment, useMemo } from "react";
import katex from "katex";
import "katex/dist/katex.min.css";
import "./MathContent.css";

type MathFormulaProps = {
  math: string;
  display?: boolean;
  ariaLabel?: string;
  className?: string;
};

/** Corrige escapes duplicados frecuentes al atravesar JSON, sin alterar saltos LaTeX. */
export function normalizeLatex(source: string): string {
  let value = source.trim();
  if (value.startsWith("$$") && value.endsWith("$$")) value = value.slice(2, -2);
  else if (value.startsWith("$") && value.endsWith("$")) value = value.slice(1, -1);
  else if (
    (value.startsWith("\\(") && value.endsWith("\\)")) ||
    (value.startsWith("\\[") && value.endsWith("\\]"))
  ) {
    value = value.slice(2, -2);
  }

  return value
    .replace(/\\\\(?=[A-Za-z])/g, "\\")
    .replace(/\\(mathbb|mathbf|mathrm)([A-Z0-9])\b/g, "\\$1{$2}")
    .replace(/\\text\{✸\}|✸/g, "\\star")
    .replace(/○/g, "\\bigcirc");
}

export function MathFormula({
  math,
  display = false,
  ariaLabel,
  className = "",
}: MathFormulaProps) {
  const normalized = normalizeLatex(math);
  const rendered = useMemo(() => {
    try {
      return {
        html: katex.renderToString(normalized, {
          displayMode: display,
          throwOnError: true,
          strict: "warn",
          trust: false,
          output: "htmlAndMathml",
        }),
        failed: false,
      };
    } catch {
      return { html: "", failed: true };
    }
  }, [display, normalized]);

  if (rendered.failed) {
    return (
      <span
        className={`math-fallback ${display ? "math-display" : ""} ${className}`.trim()}
        aria-label={ariaLabel ?? normalized}
        data-math-error="true"
      >
        {normalized}
      </span>
    );
  }

  return (
    <span
      className={`math-rendered ${display ? "math-display" : ""} ${className}`.trim()}
      aria-label={ariaLabel}
      dangerouslySetInnerHTML={{ __html: rendered.html }}
    />
  );
}

type MathTextProps = {
  text: string;
  className?: string;
};

/** Renderiza texto mixto con $, $$, \(...\) y \[...\] desde una sola implementación. */
export function MathText({ text, className = "" }: MathTextProps) {
  // Un \$ dentro de la expresión es moneda, no el delimitador de cierre.
  const tokens = text.split(
    /(\$\$(?:\\\$|[\s\S])*?\$\$|\\\[[\s\S]+?\\\]|(?<!\\)\$(?:\\\$|[^$\n])+?(?<!\\)\$|\\\([\s\S]+?\\\))/g,
  );
  return (
    <span className={className}>
      {tokens.map((token, index) => {
        let math: string | null = null;
        let display = false;
        if (token.startsWith("$$") && token.endsWith("$$")) {
          math = token.slice(2, -2);
          display = true;
        } else if (token.startsWith("\\[") && token.endsWith("\\]")) {
          math = token.slice(2, -2);
          display = true;
        } else if (token.startsWith("$") && token.endsWith("$")) {
          math = token.slice(1, -1);
        } else if (token.startsWith("\\(") && token.endsWith("\\)")) {
          math = token.slice(2, -2);
        }

        return math === null ? (
          <Fragment key={index}>{token}</Fragment>
        ) : (
          <MathFormula key={index} math={math} display={display} />
        );
      })}
    </span>
  );
}
