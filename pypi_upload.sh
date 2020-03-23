echo "Building package..."
python setup.py sdist bdist_wheel


echo "Deploying to pypi.org..."
#twine upload dist/*
