#' Log-normalize the data
#'
#' @param expr Expression data matrix.
#'
#' @return Log-normalized expression data and boxplot.
#'
#' @export
#' @import GEOquery Biobase
#' @return the log normalized expression data and boxplot
#' @examples
#' log_normalized_data <- log_normalize_data(expression_data)

log_normalize_data <- function(expr,boxplot=TRUE) {
  log_normalized_data <- log2(expr)
  if (boxplot) {
  boxplot(log_normalized_data,outline=FALSE)
  }
  return(log_normalized_data)
}
