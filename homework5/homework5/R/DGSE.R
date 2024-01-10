#' Perform Disease Gene Set Enrichment Analysis (GSEA) using identified DEGs
#'
#' This function performs Disease GSEA on identified DEGs.
#'
#' @param DEG_results Differential expression results data frame with columns 'logFC', 'pvalue', and 'adj.P.Val'.
#' @param p_value_cutoff P-value cutoff for selecting DEGs.
#' @import DOSE
#' @return the result table of disease gene set enrichment analysis
#' @export
#'
#' @examples DGSE(DEG_results, p.cutoff=0.05)
#' DEG_results <- ...  # Your differential expression results data frame
#' DGSE(DEG_results, p_value_cutoff = 0.2)
#'
DGSE <- function(DEG_results, p_value_cutoff = 0.05){
  genelist <- as.vector(DEG_results$logFC)
  genelist <- setNames(genelist, DEG_results$Entrez_Gene_ID)
  genelist <- sort(genelist, decreasing = TRUE)
  DOSE::gseDO(genelist,
                    minGSSize     = 100,
                    pvalueCutoff  = p_value_cutoff,
                    pAdjustMethod = "BH",
                    verbose       = FALSE)
}
