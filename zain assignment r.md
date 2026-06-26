# Assignment Solution
## Estimation and Diagnostics in Linear Regression Models

**Course:** Econometrics  
**Topic:** OLS assumptions, diagnostic tests, and R estimation

---

# Part A: Conceptual Questions

## Question 1 — Classical assumptions of OLS

The classical linear regression model **Y = β₀ + β₁X₁ + … + βₖXₖ + u** relies on these assumptions:

1. **Linearity** — The model is linear in the parameters β.
2. **Random sampling** — Observations are independently drawn (cross-section) or the DGP is well defined.
3. **No perfect multicollinearity** — No regressor is an exact linear combination of others.
4. **Zero conditional mean (exogeneity)** — E(u | X) = 0; errors are uncorrelated with regressors.
5. **Homoscedasticity** — Var(u | X) = σ² (constant variance).
6. **No autocorrelation** — Cov(uᵢ, uⱼ) = 0 for i ≠ j.
7. **Normality of errors** (for exact inference in small samples) — u ~ N(0, σ²).

**Why they matter:**

- Assumptions 1, 3, and 4 ensure OLS is **unbiased** and **consistent**.
- Assumptions 5 and 6 make OLS **efficient** (BLUE — Best Linear Unbiased Estimator).
- Assumption 7 allows valid **t** and **F** tests in small samples.

If assumptions 5 or 6 fail, OLS coefficients may still be unbiased, but standard errors and hypothesis tests become unreliable.

---

## Question 2 — Multicollinearity

**Definition:** Multicollinearity occurs when two or more independent variables are highly correlated with each other.

**Consequences:**
- OLS estimates remain unbiased but **standard errors increase**.
- **t-statistics fall** → variables may appear insignificant even when jointly important.
- Coefficient estimates become **unstable** and hard to interpret individually.

**Detection:**
- High pairwise correlations among regressors.
- **Variance Inflation Factor (VIF):** VIF = 1/(1 − Rⱼ²)
  - VIF = 1 → no multicollinearity
  - VIF < 5 → low
  - 5 ≤ VIF < 10 → moderate
  - VIF ≥ 10 → severe

**Correction:**
1. Drop one of the correlated variables.
2. Collect more data.
3. Combine variables (e.g., ratios).
4. Use PCA or Ridge Regression.

---

## Question 3 — Heteroscedasticity

**Definition:** Error variance is not constant: Var(uᵢ | X) = σᵢ² ≠ σ².

**Why it violates OLS:** Homoscedasticity is needed for the usual formula of standard errors to be valid. Under heteroscedasticity, OLS is still unbiased but **inefficient**, and **standard errors are wrong** → invalid t and F tests.

**Two correction methods:**

1. **Robust (White/HC) standard errors** — Corrects inference without changing coefficients. Used when the model is correctly specified but variance is non-constant.
2. **Weighted Least Squares (WLS)** — Weights observations by wᵢ = 1/σᵢ². More efficient when the variance structure is known.
3. *(Additional)* **GLS** — Generalizes WLS when Ω is known; handles heteroscedasticity and autocorrelation.

---

## Question 4 — Autocorrelation

**Definition:** Error terms are correlated across observations: Cov(uᵢ, uⱼ) ≠ 0 for i ≠ j.

**Where it occurs:** Mainly in **time-series data** (GDP, inflation), panel data, and spatial data.

**Effects:**
- OLS coefficients usually remain unbiased.
- Standard errors are **biased** → significance may be overstated (positive autocorrelation).
- OLS is no longer efficient.

**Detection — Durbin-Watson (DW):**
- DW ≈ 2 → no autocorrelation
- DW < 2 → positive autocorrelation
- DW > 2 → negative autocorrelation

---

# Part B: Critical Thinking

## Question 1 — High multicollinearity between consumption and savings

If consumption and savings are highly collinear, I would:

1. **Check** correlation matrix and VIF to confirm severity.
2. **Apply economic theory** — income, consumption, and savings are linked by accounting identities; including both as separate predictors may be redundant.
3. **Drop one variable** or use a single composite (e.g., model income using only savings or only consumption).
4. **Re-estimate** simpler models and compare adjusted R².
5. **Collect more data** or use ridge regression / PCA if both variables must stay.

---

## Question 2 — Heteroscedasticity correction preference

| Method | Best when |
|--------|-----------|
| **Robust SE** | Model form is correct; only inference needs fixing; variance form unknown |
| **WLS** | Breusch-Pagan is significant and variance can be modelled |
| **GLS** | Both heteroscedasticity and autocorrelation present |

**My choice:** **Robust standard errors** as a first step — they require fewer assumptions and fix invalid t-tests. If BP test is significant and we know variance grows with X (as in the Explanation.pdf GDP example), **WLS** is preferred for efficiency. **GLS** when autocorrelation is also detected in time-series data.

---

## Question 3 — Why data frames in R?

Econometricians prefer data frames because:

1. All variables stay **aligned** by row (no length mismatch).
2. **Formula notation** (`lm(y ~ x1 + x2, data = df)`) matches econometric writing.
3. **Missing values** are handled consistently.
4. Easy to **subset, merge, and reproduce** analyses.
5. R packages (`lm`, `ggplot2`, `dplyr`) are built for data frames.

Separate vectors are error-prone when data change.

---

# Part C: Applied R Exercises

## Data

```r
income      <- c(10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65)
consumption <- c(14, 20, 27, 31, 36, 39, 44, 47, 52, 56, 59, 63)
savings     <- c(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
df <- data.frame(income, consumption, savings)
```

**Key fact:** `income = 5 × savings` for every observation.

---

## Question 1 — OLS estimation

**Model:** income = β₀ + β₁·consumption + β₂·savings + u

```r
ols_model <- lm(income ~ consumption + savings, data = df)
summary(ols_model)
```

**Results:**

| Coefficient | Estimate | Interpretation |
|-------------|----------|----------------|
| Intercept (β₀) | ≈ 0 | Income when consumption = savings = 0 (not meaningful here) |
| consumption (β₁) | ≈ 0 | Effect of consumption on income, holding savings fixed — **unreliable** due to multicollinearity |
| savings (β₂) | **5.00** | A 1-unit increase in savings raises income by 5 units, holding consumption fixed |

**R-squared = 1.00** → perfect fit because income = 5 × savings.

**Interpretation:** The savings coefficient of 5 matches the exact data relationship. The consumption coefficient is not uniquely identified because consumption, savings, and income are almost perfectly correlated.

---

## Question 2 — Correlation matrix

```r
cor(df)
```

| | income | consumption | savings |
|---|--------|-------------|---------|
| income | 1.000 | 0.996 | **1.000** |
| consumption | 0.996 | 1.000 | 0.996 |
| savings | **1.000** | 0.996 | 1.000 |

**Comment:** All pairwise correlations exceed 0.99. Income and savings have **perfect correlation** (r = 1.00). **Multicollinearity is clearly present** and severe.

---

## Question 3 — VIF

```r
library(car)
vif(ols_model)
```

| Variable | VIF |
|----------|-----|
| consumption | **123.12** |
| savings | **123.12** |

**Interpretation:** Both VIF values are **greater than 10** → **severe multicollinearity**. Standard errors are inflated and individual coefficient estimates are unstable. This confirms the correlation matrix findings.

---

## Question 4 — Breusch-Pagan test

```r
library(lmtest)
bptest(ols_model)
```

**Result:** BP = 11.45, df = 2, **p-value = 0.0033**

**Implication:** p-value < 0.05 → **reject the null of homoscedasticity**. There is statistical evidence of heteroscedasticity. We should use **robust standard errors** or **WLS** for valid inference (as shown in Explanation.pdf when BP p < 0.05).

*Note:* Because R² = 1 and residuals are numerically zero, this test is partly driven by rounding; in real data the BP test is more interpretable.

---

## Question 5 — Durbin-Watson test

```r
dwtest(ols_model)
```

**Result:** **DW = 0.0035** (p < 0.05)

**Interpretation:** DW close to **2** means no autocorrelation (see Explanation.pdf: DW = 1.95 → no autocorrelation). Here DW ≈ 0.0035, far below 2, which technically suggests **positive autocorrelation**. However, this dataset is **cross-sectional** (not time series), and residuals are rounding noise from a perfect fit — so the DW statistic is **not economically meaningful** in this case.

---

## Question 6 — Robust standard errors

```r
library(sandwich)
library(lmtest)
coeftest(ols_model, vcov = vcovHC(ols_model, type = "HC1"))
```

**Comparison — OLS vs Robust (HC1):**

| Variable | OLS Estimate | OLS SE | Robust SE |
|----------|-------------|--------|-----------|
| Intercept | ≈ 0 | ≈ 0 | ≈ 0 |
| consumption | ≈ 0 | ≈ 0 | ≈ 0 |
| savings | **5.00** | ≈ 0 | ≈ 0 |

- **Coefficients are identical** — robust SE only changes the variance-covariance matrix, not β̂.
- Standard errors differ slightly between OLS and HC1 but are numerically tiny here because of perfect fit.
- In applied work with significant BP test, robust SE provides **valid t-tests** without respecifying the model.

---

# Conclusion

| Diagnostic | Finding |
|------------|---------|
| Multicollinearity | **Severe** (VIF ≈ 123, r ≥ 0.996) |
| Model fit | **Perfect** (R² = 1; income = 5 × savings) |
| Heteroscedasticity | **BP significant** (p = 0.003) |
| Autocorrelation | DW low but not meaningful (cross-section) |
| Recommendation | Drop redundant regressor; use `lm(income ~ savings, data = df)` |

---

# Files to reproduce

| File | Purpose |
|------|---------|
| `assignment_solution.R` | Run all Part C code in R/RStudio |
| `assignment_r_output.txt` | Expected R console output |

```r
source("/Users/eloneflax/personal/assignment_solution.R")
```

Install packages once: `install.packages(c("car", "lmtest", "sandwich"))`
