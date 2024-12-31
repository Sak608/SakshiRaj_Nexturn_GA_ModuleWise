package handler

import (
	"blog-management/model"
	"blog-management/service"
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

func CreateBlog(w http.ResponseWriter, r *http.Request) {
	var blog model.Blog
	err := json.NewDecoder(r.Body).Decode(&blog)
	if err != nil {
		http.Error(w, "Invalid payload", http.StatusBadRequest)
		return
	}

	err = service.CreateBlog(&blog)
	if err != nil {
		http.Error(w, "Failed to create blog", http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusCreated)
}

func GetBlogByID(w http.ResponseWriter, r *http.Request) {
	id, _ := strconv.Atoi(mux.Vars(r)["id"])
	blog, err := service.GetBlogByID(id)
	if err != nil {
		http.Error(w, "Failed to fetch blog", http.StatusInternalServerError)
		return
	}
	if blog == nil {
		http.Error(w, "Blog not found", http.StatusNotFound)
		return
	}
	json.NewEncoder(w).Encode(blog)
}

func GetAllBlogs(w http.ResponseWriter, r *http.Request) {
	blogs, err := service.GetAllBlogs()
	if err != nil {
		http.Error(w, "Failed to fetch blogs", http.StatusInternalServerError)
		return
	}
	json.NewEncoder(w).Encode(blogs)
}

func UpdateBlog(w http.ResponseWriter, r *http.Request) {
	id, _ := strconv.Atoi(mux.Vars(r)["id"])
	var blog model.Blog
	err := json.NewDecoder(r.Body).Decode(&blog)
	if err != nil {
		http.Error(w, "Invalid payload", http.StatusBadRequest)
		return
	}
	blog.ID = id

	err = service.UpdateBlog(&blog)
	if err != nil {
		http.Error(w, "Failed to update blog", http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusOK)
}

func DeleteBlog(w http.ResponseWriter, r *http.Request) {
	id, _ := strconv.Atoi(mux.Vars(r)["id"])
	err := service.DeleteBlog(id)
	if err != nil {
		http.Error(w, "Failed to delete blog", http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusOK)
}
