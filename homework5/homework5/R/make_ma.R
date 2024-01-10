#' Create a volcano plot with highlighted DEGs
#'
#' This function generates a volcano plot for differential gene expression results, highlighting DEGs.
#'
#' @param results Differential expression results data frame with columns 'logFC', 'pvalue', and 'adj.P.Val'.
#' @param p.cutoff p value cutoff
#' @param lfc.cutoff log fold change cutoff
#'
#' @return A MA plot with highlighted DEGs.
#'
#' @import dplyr ggplot2 magrittr
#' @export
#'
#' @examples make_ma(full_results)
make_ma <- function(results, p.cutoff=0.05, lfc.cutoff =1){
  results %>%
    mutate(Significant = adj.P.Val < p_cutoff, abs(logFC) > fc_cutoff ) %>%
    ggplot(aes(x = AveExpr, y = logFC, col=Significant)) + geom_point()
}
