# signature-management-backend

## api

## application

### use cases

- ✅ read message email with attached documentation
  - ✅ validate message sender
    - ✅ send email with message 'we received your message and process for signing documentation is being verified'
    - ✅ or send email with message about purpose of this service only for registered users
  - ✅ delete email read (move 'Arquivado' or 'Rejeitado')
  - ✅ send e-mail notifying that the message has been received and that it is being analyzed
  - ✅ save message

- [ ] Check if message is valid
  - ✅ identify process type in message text (process type enum)
  - ✅ identify process type in message text (#ID tag)
  - ✅ identify process type in message text (Situação: Em andamento)
  - ✅ identify process type in message text (Situação: Finalizado)
  - [ ] check if all pdf files were sent

- [ ] warning about message checking
  - [ ] send email with warning message about e-mail discard due to lack of process identification
  - [ ] send email with warning message about e-mail discard by ambiguous process

- [ ] validate quantity of pdf files for the process type
  - [ ] send email with warning message about e-mail discard due to lack of missing required pdf file

- [ ] validate each of the pdf files
  - [ ] send email with warning message about e-mail discard due to lack of invalid pdf file

- [ ] starts the document digital signature process

- [ ] validate digital signature on each of the PDF files if the message has been marked with #signed
  - [ ] send email to sender worning message about process interruption due to lack of invalid digital signature

- [ ] send email with message notice of documents validated and forwarded to the next step

- [ ] record process number to system controls the documentation signature flow if the message is not marked with #signed

- [ ] send email with process (number and documets) to recipient sign the documents if the message is not marked with #final
  - [ ] send email to sender worning message about process interruption due to lack of recipient email is invalid

- [ ] register the recipient for the system to accept the reply if the message is not marked with #signed or #final

- [ ] send email with signed documents to all contacts if the message has the #final tag

- [ ] wait for message

## domain - document signature management

### implementation (document signature management methods)

- ✅ validate sender
  - ✅ read sender list
  - ✅ read recipient list
  - ✅ check if sender is in 'sender list'
  - ✅ check if sender is in 'recipient list'

### ✅ schemas (signature managementent)

- ✅ Senders
- ✅ Recipients
- ✅ ProcessesType
- ✅ ProcessTypePdfFiles

### ✅ models (signature managementent)

- ✅ Senders
- ✅ Recipients
- ✅ ProcessesType
- ✅ ProcessTypePdfFiles

## infra

### database

### repository

## external

## refactory

- falta definir 'constraints' entre as Models EmailMessage e Attachments.

## CI/CD

## Docker PostgreSQL/PGAdmin

```bash
docker-compose -f ../infra/database/docker-compose.yaml --env-file ./.env --env-file ./.secrets up -d
```
