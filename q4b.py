import math

class Gps:
    def __init__(self):
        self.n, self.r = input().split()
        self.n = int(self.n)
        self.r = float(self.r)
        self.fielders = []

        for _ in range(self.n):
            x, y = map(float, input().split())
            self.fielders.append((x, y))

    def comang(self):
        self.blks = []

        for x, y in self.fielders:
            dis = math.hypot(x, y)

            if dis <= self.r:
                self.blks = [[0.0, 360.0]]
                return

            ang = math.degrees(math.atan2(y, x)) % 360
            angwid = math.degrees(math.asin(self.r / dis))

            start = (ang - angwid) % 360
            end = (ang + angwid) % 360

            if start > end:
                self.blks.append([start, 360.0])
                self.blks.append([0.0, end])
            else:
                self.blks.append([start, end])

    def mrg(self):
        if not self.blks:
            self.merged = []
            return

        self.blks.sort()
        self.merged = [self.blks[0]]

        for start, end in self.blks[1:]:
            last_start, last_end = self.merged[-1]
            if start <= last_end:
                self.merged[-1][1] = max(last_end, end)
            else:
                self.merged.append([start, end])

    def Fgps(self):
        self.dlst = []
        m = len(self.merged)

        if m == 0:
            self.dlst = [360.0]
            return

        if self.merged[0][0] > 0:
            self.dlst.append(self.merged[0][0])

        for i in range(1, m):
            prev_end = self.merged[i - 1][1]
            curr_start = self.merged[i][0]
            if curr_start > prev_end:
                self.dlst.append(curr_start - prev_end)

        last_end = self.merged[-1][1]
        first_start = self.merged[0][0]
        if last_end < 360:
            self.dlst.append((360.0 - last_end) + first_start)

    def Large(self):
        total_covered = sum(end - start for start, end in self.merged)

        if total_covered >= 360.0:
            print("0.000000")
        else:
            print(f"{max(self.dlst):.6f}")


if __name__ == "__main__":
    g = Gps()
    g.comang()
    g.mrg()
    g.Fgps()
    g.Large()
