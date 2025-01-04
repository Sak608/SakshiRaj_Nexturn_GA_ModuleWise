package middleware

import (
	"blog-management/middleware"
	"log"
	"net/http"
	"time"
)

// Logger logs the details of incoming HTTP requests
func Logger(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		log.Printf("Method: %s, URL: %s, Time: %s", r.Method, r.URL.Path, start.Format(time.RFC3339))
		next.ServeHTTP(w, r)
	})
}

// JSONHeader ensures the Content-Type is application/json
func JSONHeader(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		next.ServeHTTP(w, r)
	})
}

// AuthMiddleware adds a simple API key-based authentication
func AuthMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		apiKey := r.Header.Get("X-API-KEY")
		if apiKey != "my-secret-key" {
			http.Error(w, `{"error": "Unauthorized"}`, http.StatusUnauthorized)
			return
		}
		next.ServeHTTP(w, r)
	})
}
