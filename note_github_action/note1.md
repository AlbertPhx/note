- platform to automate deveploer workflows
- CI/CD is just one of the workflows you can automatic in github action
- Test -> Build -> Deploy
- Continuous integration
  - Build -> Test -> Merge (is order matter?)
- Continuous Delivery
  - Automatically release respository
- Continuous Deployment
  - Automatically deploy to production
- Event like : PR created/ PR merged/ issue created etc

- Benefits
  1.  setup easier

```yaml
name: Super-linter

on: push
#on: triger the event
#need to have a space!
jobs:
  super-lint:
    name: Lint code base
    runs-on: ubuntu-latest
    # ubantu, windows or macos
    steps:
      #can run command, setup tasks OR run an action
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Sub-linter
        uses: github/super-linter@v4.10.1
        env:
          Default_Branch: main
          GITHUB_TOKEN: ${{secrets.GITHUB_TOKEN}}
```

- Super-linter just like eslink, to check your code follow the rules
- indentation is important
- one job will run on one server, runs in parallel by default
