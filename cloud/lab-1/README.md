# Лабораторная работа 1 (AWS). Отчет

## Цель
Знакомство с облачными сервисами. Понимание уровней абстракции над инфраструктурой в облаке. Формирование понимания типов потребления сервисов в сервисной-модели. 

## Задача
Сопоставить входящие данные от провайдера с его же документацией

Входные поля AWS, по которым выполнялось сопоставление:
- Product Code
- Usage Type
- [lineItem/Operation]
- lineItem/LineItemDescription

Заполняемые поля (иерархия сервисной модели):
- IT Tower
- Service Family
- Service Type
- Service Sub Type
- Service Usage Type

## Самые полезные источники информации
- https://aws.amazon.com/ru/products/?aws-products-all.sort-by=item.additionalFields.productNameLowercase&aws-products-all.sort-order=asc&awsf.re%3AInvent=*all&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all
- https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html
- https://docs.aws.amazon.com/whitepapers/latest/aws-overview/amazon-web-services-cloud-platform.html

## Как выполнялась работа

### 1. Импорт и подготовка таблицы
1) Если исходник был в CSV: импорт в Excel через Данные → Из текста/CSV, разделитель “;”.
2) Проверка, что строки корректно распарсились, а колонки соответствуют ожидаемым полям биллинга.


### 3. Сопоставление строк биллинга с сервисами AWS
Для каждой строки из биллинга:
1) Смотрел Product Code и текст в lineItem/LineItemDescription (и при наличии Operation/Usage Type).
2) По этим данным определял конкретный сервис AWS (например, EC2, S3, RDS, Data Transfer и т.п.).
3) Для уточнения использовал:
   - каталог продуктов AWS (для понимания назначения сервиса и категории),
   - справочник по сервисам AWS (для подтверждения названия/принадлежности),
   - обзорный документ по категориям AWS-сервисов (для привязки к крупным категориям и согласованности).

### 4. Заполнение 5 классификационных колонок
Правило заполнения:
- IT Tower и Service Family брались в рамках единого словаря (как в образце).
- Service Type и Service Sub Type фиксировал конкретный сервис и его подсервис.
- Service Usage Type фиксировал именно тип потребления, используя шаблоны с % там, где описание в биллинге допускает вариативность.
