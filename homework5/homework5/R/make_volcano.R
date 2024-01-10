#' Create a volcano plot with highlighted DEGs
#'
#' This function generates a volcano plot for differential gene expression results, highlighting DEGs.
#'
#' @param results Differential expression results data frame with columns 'logFC', 'pvalue', and 'adj.P.Val'.
#'
#' @return A volcano plot with highlighted DEGs.
#'
#' @import ggplot2
#' @import ggrepel
#'
#' @export
#'
#' @examples
#' de_results <- ...  # Your differential expression results data frame

make_volcano <- function(results,p_cutoff=0.05,fc_cutoff =1 ) {
    results %>%
    dplyr::mutate(Significant = adj.P.Val < p_cutoff, abs(logFC) > fc_cutoff ) %>%
    ggplot2::ggplot(aes(x = logFC, y = B, col=Significant)) + geom_point()
}
