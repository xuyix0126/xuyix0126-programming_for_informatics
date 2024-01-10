#' Perform Reactome pathway analysis
#'
#' @param DEG_results A data frame containing DEGs with columns 'Entrez_Gene_ID', 'logFC', and 'pvalue'.
#' @param p_cutoff The p-value cutoff for enrichment analysis. Default is 0.05.
#'
#' @return A data frame with Reactome pathway enrichment results.
#'
#' @import ReactomePA
#' @importFrom dplyr select
#'
#' @export
#'
#' @examples
#' DEG_results <- ...  # Your data frame with DEGs
#' result <- do_reactome_analysis(top_genes, p_value_cutoff = 0.05)


reactome_path <- function(DEG_results,p_cutoff=0.05){
  de <- DEG_results$Entrez_Gene_ID
  enrich_result <- ReactomePA::enrichPathway(gene=de, pvalueCutoff = p_cutoff, readable=TRUE)
  return(enrich_result)
}
