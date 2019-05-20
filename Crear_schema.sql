create table project (
    name        text primary key,
    description text,
    deadline    date
);

create table task (
    id           integer primary key autoincrement not null,
    Dorsal    integer default 1,
    Nombres       text,
    Posicion    text,
    PasesBuenos date,
    PasesTotales date,
    Efectividad date
);
