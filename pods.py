# import subprocess

sPodName = raw_input("name of pod to add fields to: ")

aFields = []
aValues = []


def fieldsToAdd():
    global aFields

    sFieldName = raw_input("field-name (empty for continue): ")
    print(sFieldName)

    if sFieldName == '':
        valuesToAdd()
    else:
        aFields.append(sFieldName)
        fieldsToAdd()


def valuesToAdd():
    global aValues, aFields
    for (i, item) in enumerate(aFields):
        sValueName = raw_input(item + " -Value: ")
        aValues.append(sValueName)

    output()


def output():
    global aFields, aValues, sPodName
    raw_input("everything alright?? CTRL C to cancel")
    print(aFields, aValues, sPodName)

    # notifySend = ['notify-send', title, msg]
    # process = subprocess.Popen(notifySend, stdout=subprocess.PIPE)
    # output = process.communicate()[0]


fieldsToAdd()
