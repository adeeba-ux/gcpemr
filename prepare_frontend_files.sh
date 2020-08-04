for fname in ./ProntoPlus/Views/*.ui; do
  pyname="${fname%.*}.py"
  echo "Converting ${fname} to ${pyname}..."
  pyside2-uic "$fname" -o "$pyname"
done

echo "Changing assets_rc import to ProntoPlus.Views.assets_rc..."
sed -i '18s/.*/import ProntoPlus.Views.assets_rc/' ./ProntoPlus/Views/main.py
sed -i '18s/.*/import ProntoPlus.Views.assets_rc/' ./ProntoPlus/Views/patients_page.py
sed -i '18s/.*/import ProntoPlus.Views.assets_rc/' ./ProntoPlus/Views/patients_form_page.py

echo "Creating assets module in ./ProntoPlus/Views/assets_rc/..."
pyside2-rcc ./ProntoPlus/Views/assets_rc/assets.qrc -o ./ProntoPlus/Views/assets_rc/assets_rc.py

echo "Done."