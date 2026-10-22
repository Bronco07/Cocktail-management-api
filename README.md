# Cocktail Bar Management API 🍹

RESTful API stworzone w ramach zadania rekrutacyjnego przy użyciu **Django REST Framework**. Aplikacja umożliwia zarządzanie bazą koktajli oraz składników, uwierzytelnianie użytkowników za pomocą JWT oraz pełną dokumentację w Swaggerze.

---

## 🛠️ Funkcjonalności

- **Zarządzanie Składnikami (`/api/ingredients/`):** Przeglądanie, dodawanie, edycja i usuwanie składników.
- **Zarządzanie Koktajlami (`/api/cocktails/`):** Złożona relacja Wiele-do-Wielu (Many-to-Many) łącząca koktajle ze składnikami i ich proporcjami.
- **Filtrowanie i Wyszukiwanie:** Moźliwość filtrowania koktajli po kategorii/składnikach oraz wyszukiwania tekstowego po nazwie/instrukcji.
- **Autoryzacja & Uprawnienia:**
  - Odczyt (GET) dostępny dla wszystkich użytkowników.
  - Tworzenie (POST) wymaga zalogowanego konta.
  - Modyfikacja i usuwanie (PUT/PATCH/DELETE) dozwolone wyłącznie dla **autora koktajlu** lub **administratora**.
- **Dokumentacja Swagger UI:** Interaktywny interfejs OpenAPI wygenerowany za pomocą `drf-spectacular`.
- **JWT Authentication:** Bezpieczne logowanie tokenowe z wykorzystaniem `rest_framework_simplejwt`.

---

## 🚀 Uruchomienie lokalne

### 1. Wymagania
- Python 3.10+
- Wirtualne środowisko (`venv`)

### 2. Instalacja i konfiguracja

Pobierz repozytorium i przejdź do katalogu projektu:

```bash
git clone <https://github.com/Bronco07/Cocktail-management-api>
cd cocktail_project