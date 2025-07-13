import subprocess

commands = [
    "pveum user add terraform@pam",
    "pveum role add terraform -privs \"Datastore.AllocateSpace Datastore.Audit Pool.Allocate SDN.Use Sys.Audit Sys.Console Sys.Modify Sys.PowerMgmt VM.Allocate VM.Audit VM.Clone VM.Config.CDROM VM.Config.CPU VM.Config.Cloudinit VM.Config.Disk VM.Config.HWType VM.Config.Memory VM.Config.Network VM.Config.Options VM.Migrate VM.Monitor VM.PowerMgmt\"",
    "pveum group add terraform",
    "pveum acl modify / --groups terraform --roles terraform --propagate 1",
    "pveum user modify terraform@pam -group terraform",
    "pveum user token add terraform@pam terraform-token --privsep=0"
]

for cmd in commands:
    print(f"\n🔨 Executing: {cmd}")
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.stdout:
        print(f"👍 Output:\n{result.stdout.strip()}")
    if result.stderr:
        print(f"⛔ Error:\n{result.stderr.strip()}")
