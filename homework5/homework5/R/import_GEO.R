#' @title Importing GEO object and files
#'
#' @param GEO_ID GEO ID for the dataset
#'
#' \itemize{
#'   \item \code{Phenotype_data}: Phenotype data.
#'   \item \code{Expression_data}: Expression data.
#'   \item \code{Annotation_data}: Annotation data.
#' }
#'
#' @import GEOquery Biobase
#' @return A list of Expression, Phenotype and Annotation data
#' @export
#'
#' @examples
#' my_id <- "GSE33126"
#' import_GEO(my_id)


import_GEO <- function(GEO_ID="GSE33126"){
  gse<-GEOquery::getGEO(GEO_ID)
  gse<-gse[[1]]
  subj<-Biobase::pData(gse)
  expr<-Biobase::exprs(gse)
  annot<-Biobase::fData(gse)
  out_list<-list('Phenotype_data' = subj,
                 'Expression_data' = expr,
                 'Annotation_data' = annot)
  return(out_list)
}

