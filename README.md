# STIMUL FOOD — сайт для инвестора

## Что внутри

- `src` — редактируемая версия.
- `dist` — готовая публикация.
- `dist/downloads` — три основных документа инвестора.

## Перед публикацией

1. В `src/assets/config.js` укажите адрес клиентского сайта и адрес формы.
2. Запустите `python build.py`.
3. Загрузите проект в GitHub.
4. Включите GitHub Pages через готовый сценарий `.github/workflows/pages.yml`.

Сайт инвестора содержит переход на клиентский сайт. Клиентский сайт обратной ссылки не содержит.

## Рабочая форма через Cloudflare Pages

Проект содержит функцию `functions/api/lead.js` и структуру базы `schema.sql`. Подключите к проекту Cloudflare Pages базу D1 под именем `DB`. После этого форма будет сохранять обращения по адресу `/api/lead`.

## Публичный адрес после включения GitHub Pages

`https://castefeudal.github.io/stimul-food-investor/`

Кнопка перехода на клиентский сайт уже настроена на `https://castefeudal.github.io/stimul-food-client/`.

> На GitHub Pages серверный `/api/lead` не выполняется. В этой GitHub Pages-сборке форма использует безопасный демонстрационный fallback в браузере. Для реального приёма заявок подключите Cloudflare Pages/D1 или внешний endpoint.
