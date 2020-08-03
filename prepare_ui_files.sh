for fname in ./ProntoPlus/Views/*.ui; do
  pyname="${fname%.*}.py"
  echo $fname
  pyside2-uic "$fname" -o "$pyname"
done
sed -i '18s/.*/import ProntoPlus.Views.assets_rc/' ./ProntoPlus/Views/main.py
sed -i '18s/.*/import ProntoPlus.Views.assets_rc/' ./ProntoPlus/Views/patients_page.py
sed -i '18s/.*/import ProntoPlus.Views.assets_rc/' ./ProntoPlus/Views/patients_form_page.py

pyside2-rcc ./ProntoPlus/Views/assets_rc/assets.qrc -o ./ProntoPlus/Views/assets_rc/assets_rc.py