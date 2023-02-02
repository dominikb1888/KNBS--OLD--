#!/usr/bin/python3
import subprocess as sh


folder = "KNBS"
branch = "23S"

sh.run(['git commit',"-am 'changed description'",'&&','git push']

gh pr create --repo dominikb1888-KNBS/23S

gh pr list --repo  dominikb1888-KNBS/23S


git commit -am 'changed description' && git push

run_id = sh.run(["gh run list", f"--repo {repo}", "--jq '.[0].databaseId'","--json databaseId"])

gh run view --repo dominikb1888-KNBS/23S

gh run view 4074136334 --log-failed --repo dominikb1888-KNBS/23S

