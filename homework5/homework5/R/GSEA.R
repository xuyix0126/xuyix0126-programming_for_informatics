#' @title Perform Gene Set Enrichment Analysis (GSEA) on identified DEGs
#'
#' @param DEG_results Differential expression results data frame with columns 'logFC', 'pvalue', and 'adj.P.Val'.
#' @param p_value_cutoff P-value cutoff for selecting DEGs.
#' @import ReactomePA
#' @return A list of GSEA results.
#'
#' @export
#'
#' @examples

#' DEG_results <- ...  # Your differential expression results data frame
#' GSEA(DEG_results, p_value_cutoff = 0.05)

GSEA <- function(DEG_results, p_value_cutoff = 0.05) {
  genelist <- as.vector(DEG_results$logFC)
  genelist <- setNames(genelist, DEG_results$Entrez_Gene_ID)
  genelist <- sort(genelist, decreasing = TRUE)
  GSEA <- ReactomePA::gsePathway(genelist,
                     pvalueCutoff = p_value_cutoff,
                     pAdjustMethod = "BH",
                     verbose = FALSE)
  return(GSEA)
}
