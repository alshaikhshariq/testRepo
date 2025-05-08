
<p align="center">
  <a href="https://laravel.com" target="_blank">
    <img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo">
  </a>
</p>

<p align="center">
  <a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status"></a>
  <a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
  <a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
  <a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

---

## Laravel Social Media Post API

A mini Laravel REST API that lets authenticated users create and retrieve their social media posts with platform-based filtering, pagination, and Laravel Sanctum authentication.

---

## Tech Stack

- **Laravel:** 12.13.0
- **PHP:** 8.2.28
- **Auth:** Laravel Sanctum
- **DB:** Eloquent ORM
- **Test:** PHPUnit

---

## Installation

1. **Clone the repo:**
   ```bash
   git clone git@github.com:alshaikhshariq/testRepo.git
   cd testRepo
   ```

2. **Install dependencies:**
   ```bash
   composer install
   ```

3. **Set up `.env`:**
   ```bash
   cp .env.example .env
   php artisan key:generate
   ```

4. **Configure DB in `.env`**, then run:
   ```bash
   php artisan migrate
   ```

5. **Install Sanctum:**
   ```bash
   php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
   php artisan migrate
   ```

6. **Run the server:**
   ```bash
   php artisan serve
   ```

---

## Authentication

To authenticate, register a user and generate a Sanctum token:
```php
php artisan tinker

$user = User::factory()->create(['email' => 'test@example.com', 'password' => bcrypt('password')]);
$token = $user->createToken('API Token')->plainTextToken;
```

Use the token in `Authorization: Bearer <token>` header for all API requests.

---

## API Endpoints

### `POST /api/posts`
Create a new post (requires auth)

**JSON body:**
```json
{
  "content": "Example content",
  "platform": "twitter"
}
```

### `GET /api/posts`
Get all posts by the authenticated user

**Query (optional):**
`?platform=twitter`

Includes pagination (10 per page), sorted by `posted_at` descending.

---

## Testing

Run all tests:
```bash
php artisan test
```

Covers:
- Authenticated user can create a post
- Guest cannot create a post

---

## Postman

A Postman collection is available in the `postman/` directory or can be imported using this link:

> _curl --location 'http://127.0.0.1:8000/api/posts' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data '{"content":"Test post", "platform":"facebook"}'


---

## License

Licensed under the [MIT license](https://opensource.org/licenses/MIT).

---
