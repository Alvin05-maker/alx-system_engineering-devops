# Web stack debugging #3

## Task
Using strace, find out why Apache is returning a `500` error. Once you find the issue, fix it and then automate it using `Puppet` (instead of using Bash as you were previously doing).

Hint:

- `strace` can attach to a current running process
You can use tmux to run `strace` in one window and `curl` in another one
Requirements:

- Your `0-strace_is_your_friend.pp` file must contain Puppet code
You can use whatever Puppet resource type you want for you fix


## Solution
The issue was found to be a typo error in the `wp-settins.php` file. A typo which suppose to be `.php` was found to be `.phpp`. Puppet manifest above is used to automate a quick fix