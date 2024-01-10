#' Perform Differential Expression Analysis
#'
#' This function performs differential expression analysis using limma.
#'
#' @param Expression_data expression matrix
#' @param Phenotype_data pheno type data
#' @param Annotation_data annotation data
#' @return a list containing differentially expressed genes and statistical results
#' @import limma dplyr
#' @importFrom stats median
#'
#' @export
#'
#' @examples
#' result <- DEG_list(Phenotype_data, Expression_data, Annotation_data)

DEG_list <- function(Phenotype_data, Expression_data,  Annotation_data, p_cutoff=0.05,fc_cutoff=1) {
  design <- model.matrix(~0+Phenotype_data$Group)
  colnames(design) <- c("Normal","Tumor") #rename
  fit <- limma::lmFit(Expression_data, design)
  contrasts <- limma::makeContrasts(Tumor - Normal, levels=design)
  fit2 <- limma::contrasts.fit(fit, contrasts)
  fit2 <- limma::eBayes(fit2)
  anno <- dplyr::select(Annotation_data,Symbol,Entrez_Gene_ID)
  fit2$genes <- anno
  full_results <- limma::topTable(fit2, number=Inf)
  full_results <- tibble::rownames_to_column(full_results,"ID")
  full_results <- full_results[!duplicated(full_results$Entrez_Gene_ID),]
  DEG_results <- full_results[full_results$adj.P.Val < p_cutoff & abs(full_results$logFC)>fc_cutoff, ]
  return(list(DEG_results, full_results))
}

