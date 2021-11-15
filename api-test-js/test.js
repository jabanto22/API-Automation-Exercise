const request = require('supertest')('http://216.10.245.166');
const { assert, expect } = require('chai');

const uuid = require("uuid4")
const unique_name = `Learn Appium Automation with Python ${uuid()}`
const unique_isbn = `ISBN ${uuid()}`
const unique_aisle = "227"
const unique_author = `Author ${uuid()}`


describe('Library API', function() {
    it('POST /Library/Addbook.php', () => {
        const data = {
            "name": unique_name,
            "isbn": unique_isbn,
            "aisle": unique_aisle,
            "author": unique_author
        };
        // Add a new book using /Library/Addbook.php endpoint and POST as request method
        return request
            .post('/Library/Addbook.php')
            .send(data) // send payload data
            .set('Accept', 'application/json')
            .expect(200, { "Msg": "successfully added", "ID": unique_isbn + unique_aisle });
    });
    it('GET /Library/GetBook.php', () => {
        // GET the book details using /Library/Getbook.php?AuthorName=<author_name> endpoint
        // and GET as request method
        request
        .get(`/Library/GetBook.php?AuthorName=${unique_author}`)
        .end((err, res) => {
            expect(200, { "book_name": unique_name, "isbn": unique_isbn, "aisle": unique_aisle});
        });
    });
});