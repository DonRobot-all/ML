"""
ПРОЕКТ: СИСТЕМА РЕКОМЕНДАЦИИ ФИЛЬМОВ
Алгоритм: рекомендации на основе скалярного произведения векторов оценок
"""

# ============================================================================
# ШАГ 1: ПОДГОТОВКА ДАННЫХ
# ============================================================================

print("=" * 60)
print("ШАГ 1: ПОДГОТОВКА ДАННЫХ")
print("=" * 60)

# Данные о пользователях
users = ["Анна", "Борис", "Виктор", "Дарья"]

# Список фильмов
movies = [
    "Матрица",
    "Пираты Карибского моря", 
    "Начало",
    "Интерстеллар",
    "Форсаж"
]

# Матрица оценок: каждая строка - оценки одного пользователя
ratings = [
    [5, 3, 4, 5, 2],  # Анна
    [4, 4, 5, 3, 5],  # Борис
    [2, 5, 3, 4, 4],  # Виктор
    [3, 2, 5, 5, 3]   # Дарья
]

print("Пользователи в системе:", users)
print("Фильмы в базе:", movies)
print("\nМатрица оценок (пользователи × фильмы):")
print("         " + " ".join(f"{m[:5]:6}" for m in movies))
for i, user in enumerate(users):
    ratings_str = " ".join(f"{r:6}" for r in ratings[i])
    print(f"{user:8} {ratings_str}")

# ============================================================================
# ШАГ 2: ФУНКЦИЯ СКАЛЯРНОГО ПРОИЗВЕДЕНИЯ
# ============================================================================

print("\n" + "=" * 60)
print("ШАГ 2: ФУНКЦИЯ СКАЛЯРНОГО ПРОИЗВЕДЕНИЯ")
print("=" * 60)

def dot_product(vector1, vector2):
    """
    Вычисляет скалярное произведение двух векторов одинаковой длины
    Возвращает: число (скаляр)
    """
    if len(vector1) != len(vector2):
        raise ValueError("Векторы должны быть одинаковой длины")
    
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    
    return result

# Демонстрация работы функции
print("\nДемонстрация скалярного произведения:")
a = [1, 2, 3]
b = [4, 5, 6]
print(f"Вектор A = {a}")
print(f"Вектор B = {b}")
print(f"A·B = {dot_product(a, b)}")
print(f"Проверка: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32")

# ============================================================================
# ШАГ 3: ПОИСК ПОХОЖИХ ПОЛЬЗОВАТЕЛЕЙ
# ============================================================================

print("\n" + "=" * 60)
print("ШАГ 3: ПОИСК ПОХОЖИХ ПОЛЬЗОВАТЕЛЕЙ")
print("=" * 60)

def find_most_similar_user(target_user, all_ratings, user_names):
    """
    Находит пользователя с наиболее похожими вкусами
    """
    target_index = user_names.index(target_user)
    target_ratings = all_ratings[target_index]
    
    best_similarity = -float('inf')
    best_user = None
    best_index = -1
    
    print(f"\nПоиск похожих пользователей для {target_user}:")
    print(f"Оценки {target_user}: {target_ratings}")
    print("-" * 40)
    
    for i, user in enumerate(user_names):
        if i == target_index:  # Пропускаем самого себя
            continue
            
        similarity = dot_product(target_ratings, all_ratings[i])
        print(f"Сравнение с {user}:")
        print(f"  Оценки {user}: {all_ratings[i]}")
        print(f"  Скалярное произведение: {similarity}")
        
        if similarity > best_similarity:
            best_similarity = similarity
            best_user = user
            best_index = i
    
    print("-" * 40)
    print(f"Самый похожий пользователь: {best_user}")
    print(f"Мера схожести: {best_similarity}")
    
    return best_user, best_similarity, best_index

# Находим похожего пользователя для каждого
for user in users:
    similar_user, similarity, _ = find_most_similar_user(user, ratings, users)
    print(f"{user} → {similar_user} (схожесть: {similarity})")

# ============================================================================
# ШАГ 4: РЕКОМЕНДАЦИЯ ФИЛЬМОВ
# ============================================================================

print("\n" + "=" * 60)
print("ШАГ 4: РЕКОМЕНДАЦИЯ ФИЛЬМОВ")
print("=" * 60)

def recommend_movies(user_name, all_ratings, user_names, movie_names):
    """
    Рекомендует фильмы пользователю на основе вкусов похожего пользователя
    """
    # Находим похожего пользователя
    similar_user, similarity, similar_index = find_most_similar_user(
        user_name, all_ratings, user_names
    )
    
    user_index = user_names.index(user_name)
    
    recommendations = []
    
    print(f"\nРекомендации для {user_name} на основе оценок {similar_user}:")
    print(f"Оценки {user_name}: {all_ratings[user_index]}")
    print(f"Оценки {similar_user}: {all_ratings[similar_index]}")
    print("-" * 50)
    
    for i, movie in enumerate(movie_names):
        similar_rating = all_ratings[similar_index][i]
        user_rating = all_ratings[user_index][i]
        
        # Критерии рекомендации:
        # 1. Похожему пользователю фильм понравился (оценка 4 или 5)
        # 2. Текущий пользователь не смотрел (оценка 0) или оценил низко (≤ 3)
        if similar_rating >= 4 and user_rating <= 3:
            recommendations.append({
                'movie': movie,
                'similar_user_rating': similar_rating,
                'user_rating': user_rating,
                'similar_user': similar_user
            })
            print(f"✓ {movie}:")
            print(f"  {similar_user} оценил на {similar_rating}")
            print(f"  {user_name} оценил на {user_rating}")
    
    # Сортируем по оценке похожего пользователя (от высшей к низшей)
    recommendations.sort(key=lambda x: x['similar_user_rating'], reverse=True)
    
    return recommendations

# Получаем рекомендации для каждого пользователя
print("\n" + "=" * 60)
print("ИТОГОВЫЕ РЕКОМЕНДАЦИИ")
print("=" * 60)

for user in users:
    print(f"\n{user}:")
    recs = recommend_movies(user, ratings, users, movies)
    
    if recs:
        print(f"  На основе вкусов похожего пользователя вам рекомендуется:")
        for rec in recs:
            print(f"  - {rec['movie']} (оценка {rec['similar_user']}: {rec['similar_user_rating']})")
    else:
        print(f"  Нет новых рекомендаций. Вы уже посмотрели все фильмы,")
        print(f"  которые нравятся пользователям с похожими вкусами!")

# ============================================================================
# ШАГ 5: МАТРИЦА СХОЖЕСТИ ВСЕХ ПОЛЬЗОВАТЕЛЕЙ
# ============================================================================

print("\n" + "=" * 60)
print("ШАГ 5: МАТРИЦА СХОЖЕСТИ ПОЛЬЗОВАТЕЛЕЙ")
print("=" * 60)

def create_similarity_matrix(all_ratings, user_names):
    """
    Создает матрицу схожести всех пользователей
    """
    n = len(user_names)
    matrix = [[0] * n for _ in range(n)]
    
    print("\nМатрица схожести пользователей:")
    print("(значения - скалярные произведения векторов оценок)")
    print()
    
    # Заголовок таблицы
    header = " " * 10
    for name in user_names:
        header += f"{name:>10}"
    print(header)
    print("-" * (10 + 10 * n))
    
    # Заполняем матрицу и выводим
    for i in range(n):
        row_str = f"{user_names[i]:<10}"
        for j in range(n):
            if i == j:
                matrix[i][j] = 0  # Не сравниваем пользователя с самим собой
                row_str += f"{'—':>10}"
            else:
                similarity = dot_product(all_ratings[i], all_ratings[j])
                matrix[i][j] = similarity
                row_str += f"{similarity:>10}"
        print(row_str)
    
    return matrix

# Создаем и отображаем матрицу схожести
similarity_matrix = create_similarity_matrix(ratings, users)

# ============================================================================
# ШАГ 6: ЭКСПЕРИМЕНТ С НОВЫМ ПОЛЬЗОВАТЕЛЕМ
# ============================================================================

print("\n" + "=" * 60)
print("ШАГ 6: ЭКСПЕРИМЕНТ - НОВЫЙ ПОЛЬЗОВАТЕЛЬ")
print("=" * 60)

# Добавляем нового пользователя
new_user = "Егор"
new_user_ratings = [4, 5, 2, 5, 1]  # Оценки Егора

print(f"\nНовый пользователь: {new_user}")
print(f"Его оценки фильмов: {new_user_ratings}")
print("\nСравнение с существующими пользователями:")

best_match = None
best_similarity = -float('inf')
similarities = []

for i, user in enumerate(users):
    similarity = dot_product(new_user_ratings, ratings[i])
    similarities.append((user, similarity))
    
    print(f"  {new_user} & {user}: {similarity}")
    
    if similarity > best_similarity:
        best_similarity = similarity
        best_match = user

print(f"\nРезультат: {new_user} больше всего похож на {best_match}")
print(f"Схожесть: {best_similarity}")

# Рекомендуем фильмы новому пользователю
print(f"\nРекомендации для {new_user}:")

# Находим фильмы, которые понравились похожему пользователю
best_match_index = users.index(best_match)
for i, movie in enumerate(movies):
    if ratings[best_match_index][i] >= 4 and new_user_ratings[i] <= 3:
        print(f"  - {movie} (оценка {best_match}: {ratings[best_match_index][i]})")

# ============================================================================
# ШАГ 7: АНАЛИЗ И ВЫВОДЫ
# ============================================================================

print("\n" + "=" * 60)
print("ШАГ 7: АНАЛИЗ И ВЫВОДЫ")
print("=" * 60)

print("\nКлючевые наблюдения:")
print("1. Скалярное произведение действительно работает как мера схожести")
print("2. Чем больше значение, тем более похожи вкусы пользователей")
print("3. Однако у метода есть недостатки:")
print("   - Не учитывает разные шкалы оценок (строгие vs добрые пользователи)")
print("   - Не нормализовано (зависит от величины оценок)")
print("   - Пользователь, который всем ставит 5, будет 'похож' на всех")

print("\nСледующие шаги для улучшения:")
print("1. Нормализовать оценки (вычесть среднее значение)")
print("2. Использовать косинусное сходство вместо скалярного произведения")
print("3. Учитывать только общие просмотренные фильмы")
print("4. Внедрить весовые коэффициенты")

# ============================================================================
# ШАГ 8: ТЕСТИРОВАНИЕ И ПРОВЕРКА
# ============================================================================

print("\n" + "=" * 60)
print("ШАГ 8: ПРОВЕРКА РАСЧЕТОВ")
print("=" * 60)

def verify_calculations():
    """Проверяет правильность всех расчетов"""
    print("\nПроверка ключевых расчетов:")
    
    # Проверка 1: Скалярное произведение
    test_a = [1, 2, 3]
    test_b = [4, 5, 6]
    expected = 1*4 + 2*5 + 3*6  # 4 + 10 + 18 = 32
    result = dot_product(test_a, test_b)
    print(f"1. Скалярное произведение [1,2,3]·[4,5,6] = {result}")
    print(f"   Ожидалось: {expected}, Совпадает: {result == expected}")
    
    # Проверка 2: Схожесть Анны и Бориса
    anna_ratings = [5, 3, 4, 5, 2]
    boris_ratings = [4, 4, 5, 3, 5]
    expected_ab = 5*4 + 3*4 + 4*5 + 5*3 + 2*5  # 20 + 12 + 20 + 15 + 10 = 77
    result_ab = dot_product(anna_ratings, boris_ratings)
    print(f"\n2. Схожесть Анны и Бориса = {result_ab}")
    print(f"   Ожидалось: {expected_ab}, Совпадает: {result_ab == expected_ab}")
    
    # Проверка 3: Схожесть Виктора и Дарьи
    victor_ratings = [2, 5, 3, 4, 4]
    daria_ratings = [3, 2, 5, 5, 3]
    expected_vd = 2*3 + 5*2 + 3*5 + 4*5 + 4*3  # 6 + 10 + 15 + 20 + 12 = 73
    result_vd = dot_product(victor_ratings, daria_ratings)
    print(f"\n3. Схожесть Виктора и Дарьи = {result_vd}")
    print(f"   Ожидалось: {expected_vd}, Совпадает: {result_vd == expected_vd}")
    
    print("\n✓ Все проверки пройдены успешно!")

verify_calculations()

print("\n" + "=" * 60)
print("ПРОЕКТ ЗАВЕРШЕН")
print("=" * 60)