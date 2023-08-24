import subprocess


class GetSystemStates:

    def get_system_states(self):
        try:
            output = subprocess.run(["powercfg", "/a"], stdout=subprocess.PIPE)
            split_output = output.stdout.decode("utf-8").split("\n")
            available_states = []
            for line in split_output:
                if split_output.index(line) == 0:
                    continue
                if "not" in line:
                    break
                available_states.append(line.strip())
            stripped_states = [state for state in available_states if state != ""]
            return {
                "output": stripped_states,
                "error": False,
                "error_message": None
            }
        except Exception as error:
            return {
                "output": [],
                "error": True,
                "error_message": "Unable to retrieve system states information. {}".format(error)
            }

