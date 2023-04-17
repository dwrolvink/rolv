# Setup fzf
# ---------
if [[ ! "$PATH" == *$HOME/.fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}$HOME/.fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "$HOME/.fzf/shell/completion.bash" 2> /dev/null

# Kubens bug
# ----------
export KUBECTX_IGNORE_FZF=1

# Key bindings
# ------------
source "$HOME/.fzf/shell/key-bindings.bash"
