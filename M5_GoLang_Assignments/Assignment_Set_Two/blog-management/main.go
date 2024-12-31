package main

import (
	"blog-management/middleware"
	"blog-management/config"
	"blog-management/handler"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	config.InitDB()
	router := mux.NewRouter()

	router.Use(middleware.Logger)
	router.Use(middleware.JSONHeader)

	router.HandleFunc("/blog", handler.CreateBlog).Methods("POST")
	router.HandleFunc("/blog/{id:[0-9]+}", handler.GetBlogByID).Methods("GET")
	router.HandleFunc("/blogs", handler.GetAllBlogs).Methods("GET")
	router.HandleFunc("/blog/{id:[0-9]+}", handler.UpdateBlog).Methods("PUT")
	router.HandleFunc("/blog/{id:[0-9]+}", handler.DeleteBlog).Methods("DELETE")

	http.ListenAndServe(":8081", router)
}
