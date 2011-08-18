#!/bin/sh
echo 'Instalando batteryhealth'
#Check por root
if [ "$(id -u)" != "0" ]; then
   echo "No sos root, abrite" 1>&2
   exit 1
fi
INSDIR='/usr/share/batteryhealth/'
mkdir -p $INSDIR
cp main.py $INSDIR
chmod +x "${INSDIR}main.py"
cp ui.py $INSDIR
ln -sf "${INSDIR}main.py" /usr/bin/batteryhealth
echo 'Listo!'