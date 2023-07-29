contas = [(1,'1'),
          (2,'2'),
          (4,'4')]


if any(3 in conta for conta in contas):
    print("tem")
else:
    print("não tem")
