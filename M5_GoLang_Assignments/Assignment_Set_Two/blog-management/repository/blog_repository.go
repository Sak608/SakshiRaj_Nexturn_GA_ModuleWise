package repository

import (
	"blog-management/config"
	"blog-management/model"
	"database/sql"
)

func CreateBlog(blog *model.Blog) error {
	query := `INSERT INTO blogs (title, content, author) VALUES (?, ?, ?)`
	_, err := config.DB.Exec(query, blog.Title, blog.Content, blog.Author)
	return err
}

func GetBlogByID(id int) (*model.Blog, error) {
	query := `SELECT * FROM blogs WHERE id = ?`
	row := config.DB.QueryRow(query, id)

	blog := &model.Blog{}
	err := row.Scan(&blog.ID, &blog.Title, &blog.Content, &blog.Author, &blog.Timestamp)
	if err == sql.ErrNoRows {
		return nil, nil
	}
	return blog, err
}

func GetAllBlogs() ([]*model.Blog, error) {
	query := `SELECT * FROM blogs ORDER BY timestamp DESC`
	rows, err := config.DB.Query(query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var blogs []*model.Blog
	for rows.Next() {
		blog := &model.Blog{}
		err := rows.Scan(&blog.ID, &blog.Title, &blog.Content, &blog.Author, &blog.Timestamp)
		if err != nil {
			return nil, err
		}
		blogs = append(blogs, blog)
	}
	return blogs, nil
}

func UpdateBlog(blog *model.Blog) error {
	query := `UPDATE blogs SET title = ?, content = ?, author = ? WHERE id = ?`
	_, err := config.DB.Exec(query, blog.Title, blog.Content, blog.Author, blog.ID)
	return err
}

func DeleteBlog(id int) error {
	query := `DELETE FROM blogs WHERE id = ?`
	_, err := config.DB.Exec(query, id)
	return err
}
