# Cocktail Management API 🍹

REST API do zarządzania bazą koktajli oraz składników, stworzone w oparciu o **Django** i **Django REST Framework**.

## 🚀 Funkcjonalności

* **CRUD dla Koktajli i Składników:** Pełne zarządzanie zasobami wraz z relacją Many-to-Many (`CocktailIngredient` z polem ilości `amount`).
* **Autentykacja JWT:** Zabezpieczenie endpointów tworzenia/edycji przy użyciu `djangorestframework-simplejwt`.
* **Uprawnienia:** Niezalogowani użytkownicy mają dostęp tylko do odczytu (`IsAuthenticatedOrReadOnly`).
* **Automatyczne przypisywanie autora:** Nowe koktajle są automatycznie powiązywane z zalogowanym użytkownikiem (`perform_create`).
* **Filtrowanie i Wyszukiwanie:** Możliwość filtrowania po kategorii/składnikach oraz szukania po nazwach (`django-filter`).
* **Paginacja:** Wbudowane dzielenie wyników na strony (`PageNumberPagination`).
* **Dokumentacja OpenAPI / Swagger UI:** Gotowa specyfikacja API generowana przez `drf-spectacular`.
* **Testy Jednostkowe:** Zestaw automatycznych testów integracyjnych i autoryzacji (`APITestCase`).

---

## 🛠️ Stack Technologiczny

* **Language:** Python 3
* **Framework:** Django, Django REST Framework (DRF)
* **Auth:** SimpleJWT
* **Docs:** drf-spectacular (Swagger UI)
* **Database:** SQLite

---

## 💻 Uruchomienie Projektu Lokalnie

1. **Sklonuj repozytorium:**
   ```bash
   git clone <https://github.com/Bronco07/Cocktail-management-api>
   cd cocktail_project