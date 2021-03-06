Архитектура проекта:
1. Выгрузка данных из таблиц производится в виде экземпляров классов сигнатур (см. файл signatures)
Основной геттер к таблицам: получить сигнатуру программы по заданному eid (т.е. если это событие
 порождено некой И-программой, то вернется ее сигнатура).

2. Основной метод фреймфорка - make_propagation(eid, points)
См. файл propagator.py

Он выстраивает "план действий" такой, при котором событие eid произвойдет в одной из точек из списка points.
И одновременно с выстраиваением его выполняет. Это основа целенаправленных поведений.

3. Вызов этого метода провоцрует построение динамического дерева "хабов", по которому будут
 распространяться сообщения.

 Самих хабов 4 типа:
 hub_and
 hub_i
 hub_or
 hub-rw
 (см. файл hubs.py)

 Хабы содержат ссылки на своих родителей/детей. Сообщения распространяеются от детей-родителям
  и наоборот по определенным правилам. Правила обработки входящих сообщений описаны в файле
  отдельно для каждого из 4 классов хабов. Отправка узлом сообщения
  всегда спровоцирована получением им входящего сообщения, так что отправка исходящих это просто
   часть логики обработки входящих.

  Сообщения бывают двух типов ( см. messages.py):
  - с ограничением (приходит сверху, от более высокоабстрактных хабов)
  - с эземплярами выполнения программ по этим ограничениям (приходит снизу, от детей).

  Экземпляр выполнения программы ( см. prog_exemplar.py) - это результат выполнения программы, он содержит eid-ы
  событий с соотвествующими им абсолютными координатами.