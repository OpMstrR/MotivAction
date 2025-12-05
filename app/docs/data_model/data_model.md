User Story 1: Інтегрувати Покарання в UI

Сутності у цій історії:

  - User

  - Punishment

  - Quest

  - UIComponent


_________________________________________________________

Атрибути сутностей:

1. Сутність: User

Атрибут - Тип даних

id-int

username-string

email-string

level-int

penaltiesCount-int

_________________________________________________________



Сутність: Punishment (Покарання)

Атрибут-Тип даних

id-int

type-string (наприклад, warning / ban / minusXP)

description-string

issuedAt-datetime

duration-int 

userId-	int

_________________________________________________________



Сутність: Quest (Квест)

Атрибут-Тип даних

id-int

name-string

description	string

deadline-datetime

isCompleted-boolean

_________________________________________________________



Сутність: UIComponent 

Атрибут-Тип даних

id-string

type-string (button, popup, modal, block)

title-string

linkedPunishmentId-int 

_________________________________________________________


User Story 2: Додати Тригер “квест пропущено”


Сутності у цій історії:

  - User

  - Quest

  - MissedQuestTrigger (Тригер пропуску)

  - Punishment

  - Notification 

_________________________________________________________


Атрибути cутностей:

MissedQuestTrigger
Атрибут-Тип даних

id-int

questId-int

userId-int

activatedAt-datetime

status-string (“pending”, “activated”, “processed”)

_________________________________________________________


Notification

Атрибут-Тип даних

id-int

userId-int

message-string

createdAt-datetime

isRead-boolean

