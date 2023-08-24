import subprocess


class LsCPU:
    def get_cpu_info(self):
        try:
            output = subprocess.run(["lscpu"], stdout=subprocess.PIPE)
            decode_output = output.stdout.decode("utf-8")
            return {
                "output": decode_output,
                "error": False,
                "error_message": None
            }
        except Exception as error:
            return {
                "output": None,
                "error": True,
                "error_message": "Unable to retrieve cpu information. {}".format(error)
            }