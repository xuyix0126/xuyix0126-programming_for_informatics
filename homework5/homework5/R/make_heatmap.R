
#' Perform clustering and display heatmap with annotations
#'
#' This function performs clustering on the expression data and displays a heatmap with annotations.
#'
#' @param Expression_data Expression data matrix.
#' @param Phenotype_data Sample information data frame with columns 'group' and 'patient'.
#'
#' @return A heatmap displaying clustering of samples with annotations.
#'
#' @import pheatmap
#' @import dplyr
#'
#' @export
#'
#' @examples
#' expression_data <- ...  # Your expression data
#' sample_info <- ...     # Your sample information data frame
#' make_heatmap(expression_data, sample_info)

make_heatmap <- function(Expression_data, Phenotype_data) {
  corMatrix <- cor(Expression_data, use = "c")
  phenotype_data1 <- dplyr::select(Phenotype_data, source_name_ch1,characteristics_ch1.1)
  rownames(phenotype_data1) <- colnames(corMatrix)
  colnames(phenotype_data1) <- c("Group", "Patient")
  pheatmap::pheatmap(corMatrix, annotation_col = phenotype_data1)
  return(phenotype_data1)
}
