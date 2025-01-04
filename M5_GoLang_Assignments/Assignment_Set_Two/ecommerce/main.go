package main

import (
	"log"
	"net/http"

	"ecommerce/database"
	"ecommerce/handlers"
	"ecommerce/middleware"

	"github.com/gorilla/mux"
)

func main() {
	// Initialize the database
	database.InitDB()

	// Set up the router
	r := mux.NewRouter()

	// Apply global middleware
	r.Use(middleware.LoggingMiddleware)
	r.Use(middleware.BasicAuthMiddleware)

	// Define required fields for validation
	addProductRequiredFields := []string{"name", "description", "price", "stock", "category_id"}
	updateProductRequiredFields := []string{"name", "description", "price", "stock", "category_id"}

	// Routes with validation middleware
	r.Handle("/product", middleware.ValidationMiddleware(addProductRequiredFields)(http.HandlerFunc(handlers.AddProduct))).Methods("POST")
	r.Handle("/product/{id}", middleware.ValidationMiddleware(updateProductRequiredFields)(http.HandlerFunc(handlers.UpdateProduct))).Methods("PUT")

	// Routes without validation middleware
	r.HandleFunc("/product/{id}", handlers.FetchProduct).Methods("GET")
	r.HandleFunc("/product/{id}", handlers.DeleteProduct).Methods("DELETE")

	// Start the server
	log.Println("Starting server on :8081")
	log.Fatal(http.ListenAndServe(":8081", r))
}
