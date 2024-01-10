#' Visualize Reactome pathway as a network
#'
#' @param DEG_results DE analysis results
#' @param name name of the pathway(#Select one of the pathway descriptions from your over-represented Reactome Pathways)
#' @import ReactomePA
#' @return network plot of Reactome Pathway
#' @export
#'
#' @examples Network(DEG_results, "Degradation of the extracellular matrix")
Vis_network <- function(DEG_results, name){
  genelist <- as.vector(DEG_results$logFC)
  genelist <- setNames(genelist, DEG_results$Entrez_Gene_ID)
  genelist <- sort(genelist, decreasing = TRUE)
  ReactomePA::viewPathway(name,
                          readable = TRUE,
                          foldChange = genelist)
}
