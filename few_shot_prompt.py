log_prompt = """
You will receive the log of a failed CI/CD pipeline. The log contains \
unnecessary information. You'll be given a workflow to follow along with some \
examples:
1. Search for the relevant information that describes the cause of the error.
2. Identify the file in which the error is caused and which need to be \
corrected.
3. Return a Json file with the keys "relevant_infos", "explanation" and "files".\
The cause of the error (str), as described in 2., should be in "Explanation". \
The file  that caused the error should be in "Files".

Log:
 ï»¿2024-03-05T12:15:14.3880589Z Current runner version: '2.314.1'
2024-03-05T12:15:14.3912333Z ##[group]Operating System
2024-03-05T12:15:14.3913165Z Ubuntu
2024-03-05T12:15:14.3913813Z 22.04.4
2024-03-05T12:15:14.3914294Z LTS
2024-03-05T12:15:14.3914765Z ##[endgroup]
2024-03-05T12:15:14.3915323Z ##[group]Runner Image
2024-03-05T12:15:14.3915942Z Image: ubuntu-22.04
2024-03-05T12:15:14.3916515Z Version: 20240225.1.0
2024-03-05T12:15:14.3917999Z Included Software: https://github.com/actions/runner-images/blob/ubuntu22/20240225.1/images/ubuntu/Ubuntu2204-Readme.md
2024-03-05T12:15:14.3919986Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu22%2F20240225.1
2024-03-05T12:15:14.3921201Z ##[endgroup]
2024-03-05T12:15:14.3921850Z ##[group]Runner Image Provisioner
2024-03-05T12:15:14.3922557Z 2.0.359.1
2024-03-05T12:15:14.3923018Z ##[endgroup]
2024-03-05T12:15:14.3924423Z ##[group]GITHUB_TOKEN Permissions
2024-03-05T12:15:14.3926872Z Contents: read
2024-03-05T12:15:14.3927623Z Metadata: read
2024-03-05T12:15:14.3928437Z Packages: read
2024-03-05T12:15:14.3929121Z ##[endgroup]
2024-03-05T12:15:14.3933082Z Secret source: Actions
2024-03-05T12:15:14.3933906Z Prepare workflow directory
2024-03-05T12:15:14.4695547Z Prepare all required actions
2024-03-05T12:15:14.4888507Z Getting action download info
2024-03-05T12:15:14.6541176Z Download action repository 'actions/checkout@v2' (SHA:ee0669bd1cc54295c223e0bb666b733df41de1c5)
2024-03-05T12:15:14.9348908Z Complete job name: build
2024-03-05T12:15:15.0411740Z ##[group]Run actions/checkout@v2
2024-03-05T12:15:15.0412392Z with:
2024-03-05T12:15:15.0413109Z   token: ***
2024-03-05T12:15:15.0413599Z   repository: SomeOwner/SomeRepo
2024-03-05T12:15:15.0414241Z   ssh-strict: true
2024-03-05T12:15:15.0414703Z   persist-credentials: true
2024-03-05T12:15:15.0415231Z   clean: true
2024-03-05T12:15:15.0415638Z   fetch-depth: 1
2024-03-05T12:15:15.0416060Z   lfs: false
2024-03-05T12:15:15.0416451Z   submodules: false
2024-03-05T12:15:15.0416927Z   set-safe-directory: true
2024-03-05T12:15:15.0417454Z ##[endgroup]
2024-03-05T12:15:15.3693973Z Syncing repository: SomeOwner/SomeRepo
2024-03-05T12:15:15.3696341Z ##[group]Getting Git version info
2024-03-05T12:15:15.3697452Z Working directory is '/home/runner/work/SomeRepo/SomeRepo'
2024-03-05T12:15:15.3698715Z [command]/usr/bin/git version
2024-03-05T12:15:15.3858670Z git version 2.43.2
2024-03-05T12:15:15.3885930Z ##[endgroup]
2024-03-05T12:15:15.3904394Z Temporarily overriding HOME='/home/runner/work/_temp/f596c1c4-b9e1-46e0-b90d-ea1163081438' before making global git config changes
2024-03-05T12:15:15.3906227Z Adding repository directory to the temporary git global config as a safe directory
2024-03-05T12:15:15.3908788Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/SomeRepo/SomeRepo
2024-03-05T12:15:15.3956440Z Deleting the contents of '/home/runner/work/SomeRepo/SomeRepo'
2024-03-05T12:15:15.3961679Z ##[group]Initializing the repository
2024-03-05T12:15:15.3966061Z [command]/usr/bin/git init /home/runner/work/SomeRepo/SomeRepo
2024-03-05T12:15:15.4062417Z hint: Using 'master' as the name for the initial branch. This default branch name
2024-03-05T12:15:15.4063927Z hint: is subject to change. To configure the initial branch name to use in all
2024-03-05T12:15:15.4065469Z hint: of your new repositories, which will suppress this warning, call:
2024-03-05T12:15:15.4066424Z hint:
2024-03-05T12:15:15.4067180Z hint:      git config --global init.defaultBranch <name>
2024-03-05T12:15:15.4067974Z hint:
2024-03-05T12:15:15.4068792Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2024-03-05T12:15:15.4070416Z hint: 'development'. The just-created branch can be renamed via this command:
2024-03-05T12:15:15.4071408Z hint:
2024-03-05T12:15:15.4071949Z hint:      git branch -m <name>
2024-03-05T12:15:15.4075546Z Initialized empty Git repository in /home/runner/work/SomeRepo/SomeRepo/.git/
2024-03-05T12:15:15.4088781Z [command]/usr/bin/git remote add origin https://github.com/SomeOwner/SomeRepo
2024-03-05T12:15:15.5198048Z ##[endgroup]
2024-03-05T12:15:15.5199096Z ##[group]Disabling automatic garbage collection
2024-03-05T12:15:15.5200143Z [command]/usr/bin/git config --local gc.auto 0
2024-03-05T12:15:15.5201115Z ##[endgroup]
2024-03-05T12:15:15.5201827Z ##[group]Setting up auth
2024-03-05T12:15:15.5202806Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-03-05T12:15:15.5205178Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-03-05T12:15:15.5207830Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-03-05T12:15:15.5210802Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-03-05T12:15:15.5213797Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2024-03-05T12:15:15.5215295Z ##[endgroup]
2024-03-05T12:15:15.5216025Z ##[group]Fetching the repository
2024-03-05T12:15:15.5218447Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --progress --no-recurse-submodules --depth=1 origin +333d436a47062b3f68d90522ebd0f8094499110f:refs/remotes/origin/main
2024-03-05T12:15:15.8537720Z remote: Enumerating objects: 8, done.
2024-03-05T12:15:15.8538391Z remote: Counting objects:  12% (1/8)
2024-03-05T12:15:15.8538978Z remote: Counting objects:  25% (2/8)
2024-03-05T12:15:15.8539542Z remote: Counting objects:  37% (3/8)
2024-03-05T12:15:15.8540107Z remote: Counting objects:  50% (4/8)
2024-03-05T12:15:15.8540653Z remote: Counting objects:  62% (5/8)
2024-03-05T12:15:15.8541215Z remote: Counting objects:  75% (6/8)
2024-03-05T12:15:15.8541795Z remote: Counting objects:  87% (7/8)
2024-03-05T12:15:15.8542352Z remote: Counting objects: 100% (8/8)
2024-03-05T12:15:15.8542944Z remote: Counting objects: 100% (8/8), done.
2024-03-05T12:15:15.8543565Z remote: Compressing objects:  20% (1/5)
2024-03-05T12:15:15.8544158Z remote: Compressing objects:  40% (2/5)
2024-03-05T12:15:15.8544754Z remote: Compressing objects:  60% (3/5)
2024-03-05T12:15:15.8545358Z remote: Compressing objects:  80% (4/5)
2024-03-05T12:15:15.8545944Z remote: Compressing objects: 100% (5/5)
2024-03-05T12:15:15.8546570Z remote: Compressing objects: 100% (5/5), done.
2024-03-05T12:15:15.8547619Z remote: Total 8 (delta 0), reused 4 (delta 0), pack-reused 0
2024-03-05T12:15:15.8658809Z From https://github.com/SomeOwner/SomeRepo
2024-03-05T12:15:15.8660050Z  * [new ref]         333d436a47062b3f68d90522ebd0f8094499110f -> origin/main
2024-03-05T12:15:15.8672014Z ##[endgroup]
2024-03-05T12:15:15.8672703Z ##[group]Determining the checkout info
2024-03-05T12:15:15.8674593Z ##[endgroup]
2024-03-05T12:15:15.8675207Z ##[group]Checking out the ref
2024-03-05T12:15:15.8679816Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2024-03-05T12:15:15.8733130Z Switched to a new branch 'main'
2024-03-05T12:15:15.8734095Z branch 'main' set up to track 'origin/main'.
2024-03-05T12:15:15.8740077Z ##[endgroup]
2024-03-05T12:15:15.8786527Z [command]/usr/bin/git log -1 --format='%H'
2024-03-05T12:15:15.8863482Z '333d436a47062b3f68d90522ebd0f8094499110f'
2024-03-05T12:15:15.9182412Z ##[group]Run git config --local user.email "action@github.com"
2024-03-05T12:15:15.9183302Z git config --local user.email "action@github.com"
2024-03-05T12:15:15.9184027Z git config --local user.name "GitHub Action"
2024-03-05T12:15:15.9226352Z shell: /usr/bin/bash -e
2024-03-05T12:15:15.9226821Z ##[endgroup]
2024-03-05T12:15:15.9480431Z ##[group]Run echo "print(os.getcwd())" > faulty.py
2024-03-05T12:15:15.9481276Z echo "print(os.getcwd())" > faulty.py
2024-03-05T12:15:15.9504474Z shell: /usr/bin/bash -e
2024-03-05T12:15:15.9504914Z ##[endgroup]
2024-03-05T12:15:15.9582268Z ##[group]Run git add faulty.py
2024-03-05T12:15:15.9582757Z git add faulty.py
2024-03-05T12:15:15.9583198Z git commit -m "Add faulty.py"
2024-03-05T12:15:15.9583676Z git push
2024-03-05T12:15:15.9604945Z shell: /usr/bin/bash -e
2024-03-05T12:15:15.9606009Z ##[endgroup]
2024-03-05T12:15:15.9719866Z [main f6d0a35] Add faulty.py
2024-03-05T12:15:15.9720514Z  1 file changed, 1 insertion(+)
2024-03-05T12:15:15.9721063Z  create mode 100644 faulty.py
2024-03-05T12:15:16.6512714Z To https://github.com/SomeOwner/SomeRepo
2024-03-05T12:15:16.6513579Z    333d436..f6d0a35  main -> main
2024-03-05T12:15:16.6546402Z ##[group]Run python faulty.py
2024-03-05T12:15:16.6547081Z python faulty.py
2024-03-05T12:15:16.6574673Z shell: /usr/bin/bash -e
2024-03-05T12:15:16.6575241Z ##[endgroup]
2024-03-05T12:15:16.7905537Z Traceback (most recent call last):
2024-03-05T12:15:16.7906877Z   File "/home/runner/work/SomeRepo/SomeRepo/faulty.py", line 1, in <module>
2024-03-05T12:15:16.7907990Z     print(os.getcwd())
2024-03-05T12:15:16.7908846Z NameError: name 'os' is not defined
2024-03-05T12:15:16.8033229Z ##[error]Process completed with exit code 1.
2024-03-05T12:15:16.8146363Z Post job cleanup.
2024-03-05T12:15:16.9487687Z [command]/usr/bin/git version
2024-03-05T12:15:16.9549525Z git version 2.43.2
2024-03-05T12:15:16.9599494Z Temporarily overriding HOME='/home/runner/work/_temp/f7be9b84-256d-4ad4-91d1-1f56d515e70a' before making global git config changes
2024-03-05T12:15:16.9601538Z Adding repository directory to the temporary git global config as a safe directory
2024-03-05T12:15:16.9604870Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/SomeRepo/SomeRepo
2024-03-05T12:15:16.9655963Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-03-05T12:15:16.9702974Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-03-05T12:15:16.9992155Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-03-05T12:15:17.0028803Z http.https://github.com/.extraheader
2024-03-05T12:15:17.0042145Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2024-03-05T12:15:17.0090536Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-03-05T12:15:17.0813744Z Cleaning up orphan processes

Output:
{
  "relevant_infos": '''2024-03-05T12:15:16.7905537Z Traceback (most recent call last):
2024-03-05T12:15:16.7906877Z   File "/home/runner/work/SomeRepo/SomeRepo/faulty.py", line 1, in <module>
2024-03-05T12:15:16.7907990Z     print(os.getcwd())
2024-03-05T12:15:16.7908846Z NameError: name 'os' is not defined''',
  "explanation": "The error is caused by a NameError in the file faulty.py. The import statement for the os module is missing.",
  "files": "faulty.py"
}

Log:
2024-03-06T11:17:05.3741676Z Prepare all required actions
2024-03-06T11:17:05.3937498Z Getting action download info
2024-03-06T11:17:05.5489008Z Download action repository 'actions/checkout@v2' (SHA:ee0669bd1cc54295c223e0bb666b733df41de1c5)
2024-03-06T11:17:05.8472053Z Complete job name: build
2024-03-06T11:17:05.9564088Z ##[group]Run actions/checkout@v2
2024-03-06T11:17:05.9564761Z with:
2024-03-06T11:17:05.9565511Z   token: ***
2024-03-06T11:17:05.9566010Z   repository: TimoKubera/broken_webhooks
2024-03-06T11:17:05.9566655Z   ssh-strict: true
2024-03-06T11:17:05.9567144Z   persist-credentials: true
2024-03-06T11:17:05.9567706Z   clean: true
2024-03-06T11:17:05.9568101Z   fetch-depth: 1
2024-03-06T11:17:05.9568526Z   lfs: false
2024-03-06T11:17:05.9568935Z   submodules: false
2024-03-06T11:17:05.9569410Z   set-safe-directory: true
2024-03-06T11:17:05.9569925Z ##[endgroup]
2024-03-06T11:17:06.3763952Z Syncing repository: TimoKubera/broken_webhooks
2024-03-06T11:17:06.3766086Z ##[group]Getting Git version info
2024-03-06T11:17:06.3767038Z Working directory is '/home/runner/work/broken_webhooks/broken_webhooks'
2024-03-06T11:17:06.3768064Z [command]/usr/bin/git version
2024-03-06T11:17:06.3768484Z git version 2.43.2
2024-03-06T11:17:06.3769436Z ##[endgroup]
2024-03-06T11:17:06.3783600Z Temporarily overriding HOME='/home/runner/work/_temp/de9fe756-4444-4472-84b9-a0e06916e201' before making global git config changes
2024-03-06T11:17:06.3785151Z Adding repository directory to the temporary git global config as a safe directory
2024-03-06T11:17:06.3786621Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/broken_webhooks/broken_webhooks
2024-03-06T11:17:06.3787903Z Deleting the contents of '/home/runner/work/broken_webhooks/broken_webhooks'
2024-03-06T11:17:06.3789063Z ##[group]Initializing the repository
2024-03-06T11:17:06.3789809Z [command]/usr/bin/git init /home/runner/work/broken_webhooks/broken_webhooks
2024-03-06T11:17:06.3791006Z hint: Using 'master' as the name for the initial branch. This default branch name
2024-03-06T11:17:06.3792030Z hint: is subject to change. To configure the initial branch name to use in all
2024-03-06T11:17:06.3793005Z hint: of your new repositories, which will suppress this warning, call:
2024-03-06T11:17:06.3793678Z hint:
2024-03-06T11:17:06.3794190Z hint:      git config --global init.defaultBranch <name>
2024-03-06T11:17:06.3794726Z hint:
2024-03-06T11:17:06.3795334Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2024-03-06T11:17:06.3796363Z hint: 'development'. The just-created branch can be renamed via this command:
2024-03-06T11:17:06.3797064Z hint:
2024-03-06T11:17:06.3797419Z hint:      git branch -m <name>
2024-03-06T11:17:06.3798175Z Initialized empty Git repository in /home/runner/work/broken_webhooks/broken_webhooks/.git/
2024-03-06T11:17:06.3799333Z [command]/usr/bin/git remote add origin https://github.com/TimoKubera/broken_webhooks
2024-03-06T11:17:06.3800752Z ##[endgroup]
2024-03-06T11:17:06.3801422Z ##[group]Disabling automatic garbage collection
2024-03-06T11:17:06.3802364Z [command]/usr/bin/git config --local gc.auto 0
2024-03-06T11:17:06.3803143Z ##[endgroup]
2024-03-06T11:17:06.3803724Z ##[group]Setting up auth
2024-03-06T11:17:06.3804515Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-03-06T11:17:06.3806410Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-03-06T11:17:06.3908746Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-03-06T11:17:06.3960150Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-03-06T11:17:06.4384654Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2024-03-06T11:17:06.4386097Z ##[endgroup]
2024-03-06T11:17:06.4386737Z ##[group]Fetching the repository
2024-03-06T11:17:06.4388831Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --progress --no-recurse-submodules --depth=1 origin +f13f7ac68173772c61bed7ac8a34c7e65d07eb28:refs/remotes/origin/main
2024-03-06T11:17:07.6466517Z remote: Enumerating objects: 8, done.
2024-03-06T11:17:07.6467481Z remote: Counting objects:  12% (1/8)
2024-03-06T11:17:07.6468146Z remote: Counting objects:  25% (2/8)
2024-03-06T11:17:07.6468798Z remote: Counting objects:  37% (3/8)
2024-03-06T11:17:07.6469424Z remote: Counting objects:  50% (4/8)
2024-03-06T11:17:07.6470058Z remote: Counting objects:  62% (5/8)
2024-03-06T11:17:07.6470694Z remote: Counting objects:  75% (6/8)
2024-03-06T11:17:07.6471361Z remote: Counting objects:  87% (7/8)
2024-03-06T11:17:07.6471985Z remote: Counting objects: 100% (8/8)
2024-03-06T11:17:07.6472645Z remote: Counting objects: 100% (8/8), done.
2024-03-06T11:17:07.6478868Z remote: Compressing objects:  20% (1/5)
2024-03-06T11:17:07.6481803Z remote: Compressing objects:  40% (2/5)
2024-03-06T11:17:07.6484534Z remote: Compressing objects:  60% (3/5)
2024-03-06T11:17:07.6487101Z remote: Compressing objects:  80% (4/5)
2024-03-06T11:17:07.6489759Z remote: Compressing objects: 100% (5/5)
2024-03-06T11:17:07.6490532Z remote: Compressing objects: 100% (5/5), done.
2024-03-06T11:17:07.6496983Z remote: Total 8 (delta 0), reused 5 (delta 0), pack-reused 0
2024-03-06T11:17:07.6590566Z From https://github.com/TimoKubera/broken_webhooks
2024-03-06T11:17:07.6591668Z  * [new ref]         f13f7ac68173772c61bed7ac8a34c7e65d07eb28 -> origin/main
2024-03-06T11:17:07.6624112Z ##[endgroup]
2024-03-06T11:17:07.6625073Z ##[group]Determining the checkout info
2024-03-06T11:17:07.6626046Z ##[endgroup]
2024-03-06T11:17:07.6626800Z ##[group]Checking out the ref
2024-03-06T11:17:07.6631663Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2024-03-06T11:17:07.6687564Z Switched to a new branch 'main'
2024-03-06T11:17:07.6688431Z branch 'main' set up to track 'origin/main'.
2024-03-06T11:17:07.6694376Z ##[endgroup]
2024-03-06T11:17:07.6743493Z [command]/usr/bin/git log -1 --format='%H'
2024-03-06T11:17:07.6777889Z 'f13f7ac68173772c61bed7ac8a34c7e65d07eb28'
2024-03-06T11:17:07.7139130Z ##[group]Run git config --local user.email "action@github.com"
2024-03-06T11:17:07.7139988Z git config --local user.email "action@github.com"
2024-03-06T11:17:07.7140700Z git config --local user.name "GitHub Action"
2024-03-06T11:17:07.7183761Z shell: /usr/bin/bash -e
2024-03-06T11:17:07.7184221Z ##[endgroup]
2024-03-06T11:17:07.7403031Z ##[group]Run echo "c = np.array([1, 2, 3]) + np.array([3, 55, 3])" > numpy_add.py
2024-03-06T11:17:07.7404191Z echo "c = np.array([1, 2, 3]) + np.array([3, 55, 3])" > numpy_add.py
2024-03-06T11:17:07.7428419Z shell: /usr/bin/bash -e 
2024-03-06T11:17:07.7428849Z ##[endgroup]
2024-03-06T11:17:07.7509286Z ##[group]Run echo "c = 3 / 0" > division.py
2024-03-06T11:17:07.7509862Z echo "c = 3 / 0" > division.py
2024-03-06T11:17:07.7534180Z shell: /usr/bin/bash -e 
2024-03-06T11:17:07.7534605Z ##[endgroup]
2024-03-06T11:17:07.7618508Z ##[group]Run git add numpy_add.py division.py
2024-03-06T11:17:07.7619254Z git add numpy_add.py division.py
2024-03-06T11:17:07.7619940Z git commit -m "Add faulty files"
2024-03-06T11:17:07.7620545Z git push
2024-03-06T11:17:07.7643042Z shell: /usr/bin/bash -e 
2024-03-06T11:17:07.7643718Z ##[endgroup]
2024-03-06T11:17:07.7767729Z [main 4e2017f] Add faulty files
2024-03-06T11:17:07.7768683Z  2 files changed, 2 insertions(+)
2024-03-06T11:17:07.7784250Z  create mode 100644 division.py
2024-03-06T11:17:07.7785613Z  create mode 100644 numpy_add.py
2024-03-06T11:17:08.2399276Z To https://github.com/TimoKubera/broken_webhooks
2024-03-06T11:17:08.2400981Z    f13f7ac..4e2017f  main -> main
2024-03-06T11:17:08.2481182Z ##[group]Run python division.py
2024-03-06T11:17:08.2481881Z python division.py
2024-03-06T11:17:08.2507029Z shell: /usr/bin/bash -e 
2024-03-06T11:17:08.2507608Z ##[endgroup]
2024-03-06T11:17:08.3414397Z Traceback (most recent call last):
2024-03-06T11:17:08.3415584Z   File "/home/runner/work/broken_webhooks/broken_webhooks/division.py", line 1, in <module>
2024-03-06T11:17:08.3416517Z     c = 3 / 0
2024-03-06T11:17:08.3417012Z ZeroDivisionError: division by zero
2024-03-06T11:17:08.3575419Z ##[error]Process completed with exit code 1.
2024-03-06T11:17:08.3813791Z Post job cleanup.
2024-03-06T11:17:08.5166619Z [command]/usr/bin/git version
2024-03-06T11:17:08.5219532Z git version 2.43.2

Output:
{
  "relevant_infos": '''2024-03-06T11:17:08.3414397Z Traceback (most recent call last):
2024-03-06T11:17:08.3415584Z   File "/home/runner/work/broken_webhooks/broken_webhooks/division.py", line 1, in <module>
2024-03-06T11:17:08.3416517Z     c = 3 / 0
2024-03-06T11:17:08.3417012Z ZeroDivisionError: division by zero''',
  "explanation": "The error is caused by a ZeroDivisionError in the file division.py. Division by zero is not allowed.",
  "files": "division.py"
}

Log:
{log}
"""