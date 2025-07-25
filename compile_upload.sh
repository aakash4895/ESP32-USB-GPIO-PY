echo "Compiling and uploading ESP32 USB GPIO Python package..."

echo "Cleaning previous builds..."
rm -rf *.egg-info build dist

echo "Compiling the package..."
# Ensure you have the necessary tools installed, e.g., setuptools, wheel
python3 setup.py sdist bdist_wheel

echo "Uploading the package to PyPI..."
# Ensure you have twine installed: pip install twine
twine upload dist/*