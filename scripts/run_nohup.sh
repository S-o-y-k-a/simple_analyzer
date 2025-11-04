
cd /home/user/simple_analyzer

source .venv/bin/activate

nohup python3 -m simple_analyzer.main > scripts/nohup.out 2>&1 &