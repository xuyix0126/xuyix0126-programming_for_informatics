#' Create a scatter plot using Principal Component Analysis (PCA) vectors
#'
#' This function performs PCA on the provided expression data and creates a scatter plot.
#'
#' @param log_normalize_data Log transformed expression data matrix.
#' @param pheno Sample information data frame with columns 'group' and 'patient'.
#'
#' @return A scatter plot of the first two principal components.
#'
#' @import ggplot2
#' @import ggrepel
#' @import dplyr
#' @importFrom stats prcomp
#'
#' @examples
#' make_pca <- pca_plot(expression_data, pheno)

make_pca <- function(log_normalize_data, phenotype_data1) {
  pca <- prcomp(t(log_normalize_data))
  data <- cbind(phenotype_data1, pca$x)
  ggplot2::ggplot(data, ggplot2::aes(x = PC1, y=PC2, col=Group,label= Patient))+
    ggplot2::geom_point() + ggrepel::geom_text_repel()
}
